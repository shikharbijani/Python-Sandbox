class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''):
        if not self.check_funds(amount):
            return False
        self.ledger.append({'amount': -amount, 'description': description})
        return True

    def get_balance(self):
        return sum(item['amount'] for item in self.ledger)

    def transfer(self, amount, category):
        if not self.check_funds(amount):
            return False
        self.withdraw(amount, f'Transfer to {category.name}')
        category.deposit(amount, f'Transfer from {self.name}')
        return True

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = self.name.center(30, '*')
        lines = [title]
        for item in self.ledger:
            desc = item['description'][:23].ljust(23)
            amt = f"{item['amount']:.2f}".rjust(7)
            lines.append(desc + amt)
        lines.append(f'Total: {self.get_balance():.2f}')
        return '\n'.join(lines)


def create_spend_chart(categories):
    spent = []
    for cat in categories:
        spent.append(sum(-item['amount'] for item in cat.ledger if item['amount'] < 0))
    total = sum(spent)

    if total > 0:
        percents = [int((s / total * 100) // 10 * 10) for s in spent]
    else:
        percents = [0] * len(categories)

    lines = ['Percentage spent by category']

    for level in range(100, -1, -10):
        row = f'{level:>3}| '
        row += ''.join('o  ' if p >= level else '   ' for p in percents)
        lines.append(row)

    lines.append('    ' + '-' * (3 * len(categories) + 1))

    names = [cat.name for cat in categories]
    longest = max(len(n) for n in names) if names else 0
    for i in range(longest):
        row = '     '
        row += ''.join((n[i] if i < len(n) else ' ') + '  ' for n in names)
        lines.append(row)

    return '\n'.join(lines)
