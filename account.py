class BankAccount:
    def __init__(self, account, amount, balance):
        self.account = account
        self.amount = amount
        self.balance = balance

    def get_balance(self):
        if (self.balance == 'closed'):
            raise ValueError('ValueError')
        return self.balance

    def open(self):
        self.balance = 0

    def deposit(self, amount):
        if(self.balance == 'closed' or amount < 0):
            raise ValueError('ValueError')
        self.balance += amount
        
    def withdraw(self, amount):
        if(self.balance == 'closed' or self.balance < amount or amount < 0):
            raise ValueError('ValueError')
        self.balance -= amount

    def close(self):
        self.balance = "closed"
