import random
import requests
import sys

def main():
    print("====F1====","1. Search Driver","2. Random Driver","3. Exit","",sep="\n")
    try:
        menu_opt=int(input("Select Option:"))
    except ValueError:
        print("Invaild option!")
    match menu_opt:

#Option 1: Driver Search
        case 1:
            driver_name=str(input("Enter driver nanme:"))    
            driver_api_1=requests.get("https://f1api.dev/api/drivers/search?q="+driver_name)
            opt_1_json=driver_api_1.json()
            if opt_1_json["drivers"][0]["name"]:
                print("Name:",opt_1_json["drivers"][0]["name"])
                print("Surname:",opt_1_json["drivers"][0]["surname"])
                print("Race Name:",opt_1_json["drivers"][0]["shortName"])
                print("Car Number:",opt_1_json["drivers"][0]["number"])
            else:
                print("Not a driver!")

#Option 2: Randoom Driver
        case 2:
            driver_api_2=requests.get("https://f1api.dev/api/drivers")
            opt_2_json=driver_api_2.json()
            r=random.randint(1,30)
            rsearch=str(opt_2_json["drivers"][r]["surname"])
            driver_api_1=requests.get("https://f1api.dev/api/drivers/search?q="+rsearch)
            opt_1_json=driver_api_1.json()
            print("Name:",opt_1_json["drivers"][0]["name"])
            print("Surname:",opt_1_json["drivers"][0]["surname"])
            print("Race Name:",opt_1_json["drivers"][0]["shortName"])
            print("Car Number:",opt_1_json["drivers"][0]["number"])

#Option 3: Exit
        case 3:
            print("Thanks For Using THe Hub!")
            sys.exit()

#Default Case
        case _:
            print("Invaild Option!")


if __name__ == "__main__":
    main()
