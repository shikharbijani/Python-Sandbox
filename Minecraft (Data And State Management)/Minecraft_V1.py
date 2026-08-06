def main(): 
    start_inv={"Wood":5,
               "Stone":3,
               "Iron":1,
               "Coal":0,
               "Iron Ore":1,
               "Pickaxe":0,
               "Sword":0} #Starting Inventory
    achivement={"Backpack":False,
                "Bazzar":False,
                "Craft":False,
                "Cook":False}
    while True:
        print("=====Menu=====","","1. Show Inventory","2.Gather Resources","3.Crafting","4. Smelting","5. Exit",sep="\n") #Prinitng Menu
        opt=int(input("Select Option:"))
        
#Option 1: Inventory
        if opt == 1:
            achivement["Backpack"]=True
            print("Inventory")
            for i in start_inv:
                print(i,start_inv[i],sep=":")
        
#Option 2: Resources
        elif opt == 2:
            achivement["Bazzar"]=True
            print("Choose resource","","1. Wood","2. Stone","3. Iron","4. Coal",sep="\n")
            res_opt=int(input("Select Option:"))
            if res_opt==1:
                qty=int(input("Quantity:"))
                start_inv["Wood"]+=qty
            elif res_opt==2:
                qty=int(input("Quantity:"))
                start_inv["Stone"]+=qty
            elif res_opt==3:
                qty=int(input("Quantity:"))
                start_inv["Iron"]+=qty
            elif res_opt==4:
                qty=int(input("Quantity:"))
                start_inv["Coal"]+=qty
        
#Option 3: Crafting
        elif opt==3:
            achivement["Craft"]=True
            print("Crafting","","1. Pickaxe","Needs","3 Wood + 2 Stone","","2. Sword","Needs","2 Wood + 1 Iron",sep="\n")
            craft_opt=int(input("Select Option:"))
            if craft_opt==1:
                if start_inv["Wood"] >= 3 and start_inv["Stone"] >=2:
                    start_inv["Wood"]-=3
                    start_inv["Stone"]-=2
                    print("Pickaxe Crafted!")
                    start_inv["Pickaxe"]+=1
                else:
                    print("Not Enough Resources")
            elif craft_opt==2:
                if start_inv["Wood"]>=2 and start_inv["Iron"]>=1:
                    start_inv["Wood"]-=2
                    start_inv["Iron"]-=1
                    print("Sword Crafted!")
                    start_inv["Sword"]+=1
                else:
                    print("Not Enough Resources")

#Option 4: Smelting
        elif opt==4:
            achivement["Cook"]=True
            print("Select Item To Smelt:","","1. Iron Ore",sep="\n")
            fur_opt=int(input("Select Option:"))
            if fur_opt==1:
                if start_inv["Coal"]>=1 and start_inv["Iron Ore"]>=1:
                    start_inv["Coal"]-=1
                    start_inv["Iron Ore"]-=1
                    start_inv["Iron"]+=1
                    print("Smelting Done!")
        
#Option 5: Exit
        elif opt==5:
            print("Achivements!") #Achivements
            if achivement["Backpack"]:
                print("We have a backpack!")
            if achivement["Bazzar"]:
                print("Bazzar Sale!")
            if achivement["Craft"]:
                print("Game name makes sense now!")
            if achivement["Cook"]:
                print("I woonder if i can use this too cook?")
            print("Thanks for Playing!")
            break
                
main()