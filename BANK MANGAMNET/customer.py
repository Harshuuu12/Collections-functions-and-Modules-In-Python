class Customer:
    def __init__(self, name, account_balance):
        self.name = name
        self.account_balance = account_balance

    def __str__(self):
        return f"Customer: {self.name}, Account Balance: {self.account_balance}"

