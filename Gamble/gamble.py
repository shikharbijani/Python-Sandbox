import random
def main():
    wallet=int(input("Place a Bet:"))
    hscore=0
    while True:
        dice_bet=int(input("Dice Number:"))
        hl=input("Higher Or Lower?:")
        dice=random.randint(1,12)
        if hl=='Higher':
            print("On the table:",dice)
            if dice >= dice_bet:
                print('You Won!')
                wallet+=int(wallet*((dice-dice_bet)/100))
                print("Current Balance:",wallet,sep="$")
                if wallet>hscore:
                    hscore=wallet
            else:
                print("Better Luck Next Time!")
                wallet-=int(wallet*((dice-dice_bet)/100))
                print("Current Balance:",wallet,sep="$")
        if hl=="Lower":
            print("On the table",dice)
            if dice <= dice_bet:
                print("You Won!")
                wallet+=int(wallet*((dice_bet-dice)/100))
                print("Current Balance:",wallet,sep="$")
                if wallet>hscore:
                    hscore=wallet
            else:
                print("Better Luck Next Time!")
                wallet-=int(wallet*((dice_bet-dice)/100))
                print("Current Balance:",wallet,sep="$")
        if wallet <= 0:
            print("Well You are broke!")
            print("Highest Amount Earned:",hscore)
            break
           
main()
