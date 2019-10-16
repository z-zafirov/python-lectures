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
        if isinstance(bills, list):
            self.bill = list(bills)
        else:
            self.bill = [bills]

    def __getitem__(self, index):
        pass

    def __len__(self):
        '''returns the number of `Bills` in the batch'''
        return len(self.bill)

    def total(self):
        '''returns the total amount of all `Bills` in the batch'''
        x = 0
        for i in self.bill:
            x = x + i
        return x

#'''
b1 = int(Bill(2))
list_bills = [b1, 5, 10, 20, 50]
bb1 = BatchBill(list_bills)
bb2 = BatchBill(b1)
print(bb1.__len__())
print(bb1.total())
print(bb2.total())
#'''

class CashDesk():
    cash_desk = {}

    def take_money(self, money):
        ''' where `money` can be either `Bill` or `BatchBill` class '''
        # check the object type - bill or batch
        # add to or increase the cash_desk list depending on the object type
        return None

    def total(self):
        ''' returns the total amount of money currenly in the desk '''
        # sum the cash_desk list
        return None

    def inspect(self):
        ''' returns a table representation of the money - for each bill, how many copies of it we have '''
        # return dictionary with key - bill value and values - bills count
        return None

'''
values = [10, 20, 50, 100, 100, 100]
bills = [Bill(value) for value in values]

batch = BatchBill(bills)

desk = CashDesk()

desk.take_money(batch)
desk.take_money(Bill(10))

print(desk.total()) # 390
desk.inspect()
'''