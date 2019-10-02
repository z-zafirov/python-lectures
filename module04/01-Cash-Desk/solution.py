class Bill():
    def __init__(self, amount):
        self.amount = amount
        try:
            if amount * 0 != 0 or amount % 1 != 0:
                raise TypeError('Non-int amount provided.')
            elif amount < 0:
                raise ValueError('Negative amount provided.')        
        except ValueError  as exc:
            self.amount = f'Exception: {exc}'
        except TypeError as exc:
            self.amount = f'Exception: {exc}'


    def __int__(self):
        return int(self.amount)

    def __str__(self):
        return str(self.amount)

    def __repr__(self):
        return f'Bill({self.amount})'

    def __hash__(self):
        return hash(self.amount)

    def __eq__(self, other):
        return (
            self.__class__ == other.__class__ and
            self.amount == other.amount
        )
'''
t1 = Bill(1.0)
print(t1)
print(t1.__eq__(t1))
'''

class BatchBill():
    def __init__(self, bills):
        self.bills = list(bills)

    def __getitem__(self, index):
        pass

    def __len__(self):
        '''returns the number of `Bills` in the batch'''
        return len(self.bills)

    def total(self):
        '''returns the total amount of all `Bills` in the batch'''
        x = 0
        for i in self.bills:
            x = x + i
        return x

'''
list_bills = [5, 10, 20, 50]
bb1 = BatchBill(list_bills)
print(bb1.__len__())
print(bb1.total())
'''

class CashDesk():

    def take_money(self, money):
        ''' where `money` can be either `Bill` or `BatchBill` class '''
        return None

    def total(self):
        ''' returns the total amount of money currenly in the desk '''
        return None

    def inspect(self):
        ''' returns a table representation of the money - for each bill, how many copies of it we have '''
        return None