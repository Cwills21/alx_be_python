class BankAccount:
    def __init__(self, account_balance ):
        self.account_balance = account_balance
    

    def deposit(self, amount):
            if amount > 0:
               self.account_balance += amount
               print(f'You just deposited {amount}')
            else:
               print('Deposite amount must be positive')
            
    def withdraw(self, amount):
           if amount <= self.account_balance:
             self.account_balance -= amount
             return True
           else:
             print('Insulficient Account Balance')
             return False
            
    def display_balance(self):
            print(f'Your current balance is {self.account_balance:2f}')