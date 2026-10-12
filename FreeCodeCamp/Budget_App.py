class Category:
    def __init__(self):
        self.ledger=[]

    def deposit(self,amount,description=""):
        self.ledger.append({'amount': amount, 'description': description})

    def withdrawn(self,amount,description=""):
        if amount<0:
            self.ledger.append({'amount': amount,'description': description})
            return True
        return False

    def get_balance(self):
        balance=0
        for i in range(len(self.ledger)):
            balance+=self.ledger[i]["amount"]
        return balance

    def tansfer(self):
        pass


def create_spend_chart(categories):
    pass

# cat=Category()
# cat.deposit(1000)
# cat.withdrawn(-500)
# print(cat.get_balance())
