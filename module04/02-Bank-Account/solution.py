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

    def deposit(self, d_amount):
        try:
            if d_amount <= 0:
                raise ValueError('Negative or null value provided for deposit amount.')
            elif d_amount > 0:
                self.balance = self.balance + d_amount
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.history_list.append(f'{timestamp} | {d_amount} {self.currency} were deposited on {self.name}\'s account.')
        except ValueError  as exc:
            self.balance = f'Exception: {exc}'

    def withdraw(self, w_amount):
        if w_amount <= 0:
            return False
        elif w_amount > 0:
            self.balance = self.balance - w_amount
            timestamp = timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.history_list.append(f'{timestamp} | {w_amount} {self.currency} were withdrawn from {self.name}\'s account.')
            return True

    def account_currency(self):
        return self.currency

    def transfer_to(self, account, t_amount):
        account_currency = account.account_currency()
        if self.balance >= t_amount and self.currency == account_currency:
            self.balance = int(self.balance - t_amount)
            account.balance = int(account.balance + t_amount)
            print('Transfer successful.')
        else:
            print('Different currencies or balance too low, transfer not successful.')


'''
o1 = BankAccount('Jack Doe', 'BGN', 30)
o2 = BankAccount('Jack Richar', 'USD', 50)
o3 = BankAccount('Jane Smith', 'BGN', 30)

print(str(o1))
o1.deposit(10)
print(str(o1))

t1 = o1.withdraw(20)
print(f'withdraw status for 20: {t1}')
print(str(o1))
t2 = o1.withdraw(-10)
print(f'withdraw status for -10: {t2}')

print(str(o1))
print(int(o1))

print(o1.history_list)

print(str(o1))
print(str(o2))
print(str(o3))
o1.transfer_to(o3, 10)
o1.transfer_to(o2, 10)
print(str(o1))
print(str(o2))
print(str(o3))
'''