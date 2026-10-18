class Category:
    def __init__(self,name):
        self.name=name
        self.ledger=[]

    def deposit(self,amount,description=""):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self,amount,description=""):
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
        if self.check_funds(amount) and amount<0:
            self.withdraw(amount,description=f"Transfer to {destination}")
            destination.deposit(amount,description=f"Transfer from {self}")
            return True
        return False

    def check_funds(self,amount):
        if self.get_balance()>=amount:
            return True
        return False

    def __str__(self):
        print(self.name.center(30,"*"))
        body=""
        for _ in self.ledger:
            print(_)
        return ""


def create_spend_chart(categories):
    pass

cat=Category("cat")
gor=Category("gor")

cat.deposit(1000)
cat.withdraw(-500)
print(cat)
