def main():
    start_inv={"Wood":0,"Stone":0,"Iron":0,"Coal":0,"Iron Ore":1,"Pickaxe":0,"Sword":0}
    achivements=[{"Msg":"Wow we have a backpack?","Status":False},
                 {"Msg":"Welcome to the Bazzar!","Status":False},
                 {"Msg":"50\% \of the game name!","Status":False},
                 {"Msg":"I wonder if i can cook in this?","Status":False}
                 ]
    while True:
        print("=====Menu=====","","1. Show Inventory","2. Resources","3. Crafting","4. Smelting","0. Exit",sep="\n")
        menu_opt=int(input("Select Option:"))
        match menu_opt:

#Option 1: Inventory            
            case 1:
                print("=====Inventory=====")
                for i in start_inv:
                    print(i,start_inv[i], sep=": ")
                if not achivements[0]["Status"]:
                    print("Achivement!:",achivements[0]["Msg"])
                    achivements[0]["Status"]=True

#Option 2: Resources
            case 2:
                print("=====Choose resource=====","","1. Wood","2. Stone","3. Iron","4. Coal",sep="\n")
                res_opt=int(input("Select Option:"))
                match res_opt:
                    case 1:
                        qty=int(input("Quantity:"))
                        start_inv["Wood"]+=qty
                    case 2:
                        qty=int(input("Quantity:"))
                        start_inv["Stone"]+=qty
                    case 3:
                        qty=int(input("Quantity:"))
                        start_inv["Iron"]+=qty
                    case 4:
                        qty=int(input("Quantity:"))
                        start_inv["Coal"]+=qty
                    case _:
                        print("Mate,we dont have that")
                if not achivements[1]["Status"]:
                    print("Achivement!:",achivements[1]["Msg"])
                    achivements[1]["Status"]=True
        
#Option 3: Crafting
            case 3:
                print("=====Crafting=====","","1. Pickaxe","Needs","3 Wood + 2 Stone","","2. Sword","Needs","2 Wood + 1 Iron",sep="\n")
                craft_opt=int(input("Select Option:"))
                match craft_opt:
                    case 1:
                        if start_inv["Wood"] >= 3 and start_inv["Stone"] >=2:
                            start_inv["Wood"]-=3
                            start_inv["Stone"]-=2
                            print("Pickaxe Crafted!")
                            start_inv["Pickaxe"]+=1
                            if not achivements[2]["Status"]:
                                print("Achivement!:",achivements[2]["Msg"])
                                achivements[2]["Status"]=True
                        else:
                            print("Not Enough Resources!")
                    case 2:
                        if start_inv["Wood"]>=2 and start_inv["Iron"]>=1:
                            start_inv["Wood"]-=2
                            start_inv["Iron"]-=1
                            print("Sword Crafted!")
                            start_inv["Sword"]+=1
                            if not achivements[2]["Status"]:
                                print("Achivement!:",achivements[2]["Msg"])
                                achivements[2]["Status"]=True
                        else:
                            print("Not Enough Resources")
                    case _:
                        print("New Crafting Recipes soon!")

#Option 4: Smelting
            case 4:
                print("=====Smelting=====","","1. Iron Ore",sep="\n")
                fur_opt=int(input("Select Option:"))
                match fur_opt:
                    case 1:
                        if start_inv["Coal"]>=1 and start_inv["Iron Ore"]>=1:
                            start_inv["Coal"]-=1
                            start_inv["Iron Ore"]-=1
                            start_inv["Iron"]+=1
                            print("Smelting Done!")
                            if not achivements[3]["Status"]:
                                print("Achivement!:",achivements[3]["Msg"])
                                achivements[3]["Status"]=True
                        else:
                            print("Not Enough Resources")

#Option 0: Exit
            case 0:
                print("Achivements!:")
                for i in range(len(achivements)):
                    if achivements[i]["Status"]:
                        print(i,achivements[i]["Msg"])
                print("Thanks For Playing!")
                break

#Option None
            case _:
                print("Not an feature!")




main()