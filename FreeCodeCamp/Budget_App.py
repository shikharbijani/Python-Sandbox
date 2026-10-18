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
        output=self.name.center(30,"*")+"\n"
        for payment in self.ledger:
            output+=f"{payment['description'][:23].ljust(23)}{payment['amount']:>7.2f}\n"
        output+=f"Total: {self.get_balance()}"
        return output


def create_spend_chart(categories):
    pass

cat=Category("cat")
gor=Category("gor")

cat.deposit(1000,"Initail Deposit")
cat.withdraw(-500,"Party")
cat.deposit(200,"Refund")
print(cat)
