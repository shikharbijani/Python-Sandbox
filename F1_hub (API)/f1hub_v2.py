import random
import sys
import requests

def main():
    while True:
        print("====F1====","1. Search Driver","2. Random Driver","3. Exit","",sep="\n")
        try:
            menu_opt=int(input("Select Option:"))
        except ValueError:
            print("Invaild option!")
    
        match menu_opt:
        
#Option 1: Search
            case 1:
                driver_name=input("Enter Driver Name:")
                driver_search(driver_name)

#Option 2: Random
            case 2:
                print("Your Driver is......")
                driver_api=requests.get("https://f1api.dev/api/drivers")
                driver_json=driver_api.json()
                try:
                    r=random.randint(0,(len(driver_json["drivers"])-1))
                except (KeyError,IndexError):
                    print("Opps!")
                rsearch=str(driver_json["drivers"][r]["surname"])
                driver_search(rsearch)

#Option 3: Exit
            case 3:
                print("Thanks For Using F1 Hub!!")
                break

#Default case
            case _:
                print("Invaild Option!")

def driver_search(name):
    api_search=requests.get("https://f1api.dev/api/drivers/search?q="+name)
    search_api=api_search.json()
    if search_api["drivers"][0]["name"]:
        display_output(search_api)
    else:
        print("Not a driver!")

def display_output(api):
    print("Name:",api["drivers"][0]["name"])
    print("Surname:",api["drivers"][0]["surname"])
    print("Race Name:",api["drivers"][0]["shortName"])
    print("Car Number",api["drivers"][0]["number"])

if __name__=="__main__":
    main()
