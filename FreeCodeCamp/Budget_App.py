class Category:
    def __init__(self):
        self.ledger=[]

    def deposit(self,amount,description=""):
        self.ledger.append({'amount': amount, 'description': description})

    def withdrawn(self,amount,description=""):
        if self.check_funds and amount<0:
            self.ledger.append({'amount': amount,'description': description})
            return True
        return False

    def get_balance(self):
        balance=0
        for i in range(len(self.ledger)):
            balance+=self.ledger[i]["amount"]
        return balance

    def transfer(self,amount,destination):
        if self.check_balance() and amount>0:
            self.withdrawn(-1*amount,description=f"Transfer to {destination}")
            destination.deposit(amount,description=f"Transfer from {self}")
            return True
        return False

    def check_funds(self,amount):
        if self.get_balance()>=amount:
            return True
        return False




def create_spend_chart(categories):
    pass

cat=Category()
gor=Category()

cat.deposit(1000)
cat.withdrawn(-500)
print(cat.get_balance())
print(cat.check_funds(500))

