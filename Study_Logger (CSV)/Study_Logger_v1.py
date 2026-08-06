import csv

def main():
    while True:
        print(f"====Study Logger====\n1.Add Session\n2.See All Sessions\n3.Exit\n")
        menu_opt=int(input("Enter Option:"))
        match menu_opt:
            case 1:
                print("====Add Session====")
                date=input("Enter Date:")
                subject=input("Enter Subject:")
                minutes=int(input("Enter Time:"))
                with open("Study Logger.csv","a",newline="") as file:
                    session_data=[date,subject,minutes]
                    writer=csv.writer(file)
                    writer.writerow(session_data)

            case 2:
                print("====Study Log====")
                with open("Study Logger.csv","r") as file:
                    reader=csv.reader(file)
                    for line in reader:
                        print(f"Date: {line[0]}\nSubject: {line[1]}\nTime: {line[2]} Minutes\n")

            case 3:
                print("Thank For Using!")
                break

            case _:
                print("Not an Option!")


if __name__=="__main__":
    main()
