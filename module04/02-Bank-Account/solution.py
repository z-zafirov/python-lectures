from datetime import datetime

class BankAccount():
    history_list = []

    def __init__(self, name, currency, balance=0):
        self.name = name
        self.currency = currency
        try:
            if balance >= 0:
                self.balance = balance
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.history_list.append(f'{timestamp} | Created {self.name}\'s account with balance of {self.balance} {self.currency}.')
            elif balance < 0:
                raise ValueError('Negative value provided for balance.')
        except ValueError  as exc:
            self.balance = f'Exception: {exc}'
    
    def __str__(self):
        return f'Bank account for {self.name} with balance of {self.balance} {self.currency}'

    def __int__(self):
        return int(self.balance)

    def deposit(self, amount):
        try:
            if amount <= 0:
                raise ValueError('Negative or null value provided for deposit amount.')
            elif amount > 0:
                self.balance = self.balance + amount
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.history_list.append(f'{timestamp} | {amount} {self.currency} were deposited on {self.name}\'s account.')
        except ValueError  as exc:
            self.balance = f'Exception: {exc}'

    def withdraw(self, amount):
        if amount <= 0:
            return False
        elif amount > 0:
            self.balance = self.balance - amount
            timestamp = timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.history_list.append(f'{timestamp} | {amount} {self.currency} were withdrawn from {self.name}\'s account.')
            return True

#'''
o1 = BankAccount('Jack Doe', 'BGN', 30)
print(str(o1))
o1.deposit(10)
print(str(o1))
t1 = o1.withdraw(20)
print(f'withdraw status for 20: {t1}')
print(str(o1))
t2 = o1.withdraw(-10)
print(f'withdraw status for -10: {t2}')
print('Testing int() and str() below:')
print(str(o1))
print(int(o1))
print('Testing the history list below:')
print(o1.history_list)
#'''