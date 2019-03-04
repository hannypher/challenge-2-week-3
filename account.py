class BankAccount:
    
    def __init__(self, balance, account):
        self.balance = balance
        self.account = account


    def open(self, account):
        self.balance = 0
        return self.account


    def get_balance(self, account, balance):
        self.balance = 0
        if (self.balance == 'closed'):
            raise ValueError('Account has been closed')
        return self.balance


    def deposit(self, amount):
        if(self.balance == 'closed' or amount < 0):
            raise ValueError('Account has been closed')
        self.balance += amount
        return self.balance

        
    def withdraw(self, amount):
        if(self.balance == 'closed' or self.balance < amount or amount < 0):
            raise ValueError('Insufficient funds')
        self.balance -= amount
        return self.balance


    def close(self, account):
        self.balance = "closed"
