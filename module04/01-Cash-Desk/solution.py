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
b1 = int(Bill(2))
list_bills = [b1, 5, 10, 20, 50]
bb1 = BatchBill(list_bills)
print(bb1.__len__())
print(bb1.total())
'''

class CashDesk():
    cash_desk = {10:2, 20:1, 50:1, 100:3}

    @classmethod
    def take_money(cls, money):
        ''' where `money` can be either `Bill` or `BatchBill` class '''
        # construct object regarding the input type - bill or batch
        if isinstance(money, list):
            money = list(money)
        else:
            money = [money]
        # remove bills from the cash_desk if there are available of that value
        for m in money:
            if m in cls.cash_desk.keys() and cls.cash_desk[m] > 0:
                cls.cash_desk[m] = cls.cash_desk[m] - 1
            else:
                print(f'There are no bills of value {m} in the cash desk.')

    @classmethod
    def total(cls):
        ''' returns the total amount of money currenly in the desk '''
        # sum the cash_desk list
        result = 0
        for x in range(len(cls.cash_desk)):
            result = result + list(cls.cash_desk.values())[x] * list(cls.cash_desk.keys())[x]
        return result

    @classmethod
    def inspect(cls):
        ''' returns a table representation of the money - for each bill, how many copies of it we have '''
        # return dictionary with key - bill value and values - bills count
        print(f'Bills of value in the cashdesk:')
        for i in range(len(cls.cash_desk)):
            count = list(cls.cash_desk.values())[i]
            value = list(cls.cash_desk.keys())[i]
            print(f'bills count: {count} | value: {value}')

'''
csh = CashDesk()
print(csh.total())
csh.take_money(100)
csh.take_money([10,50])
csh.take_money(35)
csh.take_money(50)
print(csh.total())
csh.inspect()
'''

#'''
values = [10, 20, 50, 100, 100, 100]
bills = [int(Bill(value)) for value in values]
#print(bills)

batch = BatchBill(bills)

desk = CashDesk()

desk.take_money(batch)
desk.take_money(Bill(10))

print(desk.total()) # 390
desk.inspect()
#'''