import random

def wager_percentage(p) -> int:    #Calculate the winning wager percetage based on winning probability     -p means p/12
    if 10<= p <= 12:        
        return 1.25
    elif 7<= p <= 9:
        return 1.5
    elif p == 6:
        return 2
    elif 3 <= p <= 5:
        return 3
    elif p == 2 :
        return 5
    elif p == 1:
        return 10

def probability_calc(betting_choice,betting_number) -> int:    #Calculate p for wager percentage
    if betting_choice == "Higher":
        return (12-betting_number)
    elif betting_choice == "Lower":
        return (betting_number-1)
    elif betting_choice == "Equal":
        return 1

def check_result(betting_choice,betting_number,dice) -> bool:   #Checking if player Won or Lost 
    if betting_choice == "Higher":
        if dice>betting_number:
            return True
        else:
            return False
    elif betting_choice == "Lower":
        if dice<betting_number:
            return True
        else:
            return False
    elif betting_choice == "Equal":
        if dice == betting_number:
            return True
        else:
            return False

def update_balance(balance,result,wager,wager_multiplier) -> int:   #Calculates new balance
    if result:
        balance += wager*wager_multiplier
    else:
        balance -=wager
    return balance

def bet_validation(betting_choice,betting_number) -> bool:
    if betting_choice in ["Higher","Lower","Equal"]:
        return probability_calc(betting_choice,betting_number) > 0
    else:
        return False
    
def wager_validation(balance,wager) -> None:    #Calculates if wager is valid
    return 10 <= wager <= balance
        
def main():
    balance = 1000
    while True:                                                            #Round Loop
        while True:                                                        #Wager Validation loop
            try:
                wager= int(input("Enter Wager:"))
            except ValueError:
                print("Not An Integer!")
                continue
            if wager_validation(balance,wager):
                break
            else:
                print("Invalid Wager Amount")
        while True:                                                        #Bet Validation loop
            try:
                betting_number = int(input("Enter Betting Number: "))
            except ValueError:
                print("Not An Integer!")
                continue
            betting_choice = input("Enter Betting Choice: ")
            if bet_validation(betting_choice, betting_number):
                break
            else:
                print("Invalid Bet!")  #can be a better msg!
        p=probability_calc(betting_choice,betting_number)
        wager_multiplier=wager_percentage(p)
        dice=random.randint(1,12)
        if check_result(betting_choice,betting_number,dice):
            print("Congrats! You Won!")
            result=True
        else:
            print("You Lost! Better Luck Next Time!")
            result=False
        balance=update_balance(balance,result,wager,wager_multiplier)
        print(f"You current balance is: {balance}")
        if balance <10:
            print("The balance is too low to play another round!")
            break
        next_round=input("Do you wanna play another round? (y/n):")
        if next_round == "y":
            continue
        else:
            break

if __name__=="__main__":
    main()
