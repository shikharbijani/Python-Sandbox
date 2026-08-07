import csv
import re

def main():
    while True:
        print_menus(1)
        try:
            menu_opt=int(input("Enter Option:"))
        except ValueError:
            print("Not a Option")
            continue
        match menu_opt:

#Option 1: Adding Session
            case 1:
                print_menus(2)
                date=date_validation()
                subject=input("Enter Subject:")
                minutes=minutes_validation()
                with open("Study Logger.csv","a",newline="") as file:
                    session_data=[date,subject,minutes]
                    writer=csv.writer(file)
                    writer.writerow(session_data)

#Option 2: See Sessions
            case 2:
                print_menus(3)
                with open("Study Logger.csv","r") as file:
                    reader=csv.reader(file)
                    for line in reader:
                        print(f"Date: {line[0]}\nSubject: {line[1]}\nTime: {line[2]} Minutes\n")

#Option 3: Exit
            case 3:
                print("Thanks For Using!")
                break

def date_validation():                  #Validating Date Format
    while True: 
        date_input=input("Enter Date:")
        if re.fullmatch(r"(0[1-9]|[1-2][0-9]|3[0-1])-(0[1-9]|1[0-2])-[0-9]{4}",date_input):
            return date_input
            break
        else:
            print("Please Enter in DD-MM-YYYY Format")

def minutes_validation():                   #Validating Minutes
    while True:
        try:
            minutes_input=int(input("Enter Minutes:"))
            if minutes_input < 0:
                print("Number cant be negative")
            else:
                return minutes_input
                break
        except ValueError:
            print("Please Enter A Number")

def print_menus(n):                 #Menus Printed while using the program
    if n ==1:
        print(f"====Study Logger====\n1.Add Session\n2.See Sessions\n3.Exit\n")
    elif n==2:
        print("====Add Session====")
    elif n==3:
        print("====Study Log====")

if __name__=="__main__":
    main()
