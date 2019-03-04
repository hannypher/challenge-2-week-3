class BankAccount:
    def __init__(self):
        #initialize global variable balance to be accessed by any method in this class
        self.balance = 0


    def open(self):
        self.balance = 0


    def get_balance(self):
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


    def close(self):
        self.balance = "closed"
        return self.balance
