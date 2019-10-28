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
        return self.bills[index]

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

    def take_money(self, money):
        ''' where `money` can be either `Bill` or `BatchBill` class '''
        # construct object regarding the input type - bill or batch
        if isinstance(money, int):
            self.money = [money]
        elif isinstance(money, list):
            self.money = [int(y) for y in money]
        elif isinstance(money, Bill):
            self.money = [int(money)]
        # remove bills from the cash_desk if there are available of that value
        for m in self.money:
            if m in self.cash_desk.keys() and self.cash_desk[m] > 0:
                self.cash_desk[m] = self.cash_desk[m] - 1
            else:
                print(f'There are no bills of value {m} in the cash desk.')

    def total(self):
        ''' returns the total amount of money currenly in the desk '''
        # sum the cash_desk list
        result = 0
        for x in range(len(self.cash_desk)):
            result = result + list(self.cash_desk.values())[x] * list(self.cash_desk.keys())[x]
        return result

    def inspect(self):
        ''' returns a table representation of the money - for each bill, how many copies of it we have '''
        # return dictionary with key - bill value and values - bills count
        print(f'Bills of value in the cashdesk:')
        for i in range(len(self.cash_desk)):
            count = list(self.cash_desk.values())[i]
            value = list(self.cash_desk.keys())[i]
            print(f'bills count: {count} | value: {value}')


values = [10, 20, 50, 100, 100, 100]
bills = [int(Bill(value)) for value in values]
batch = list(BatchBill(bills))
desk = CashDesk()
'''
print(desk.total())
desk.take_money(50)
desk.take_money([50, 20])
desk.take_money(Bill(10))
desk.take_money([Bill(10), (Bill(20))])
desk.take_money(BatchBill([10, 20]))
desk.take_money(BatchBill([(Bill(10)), Bill(20)]))
print(desk.total())
'''
#print(list(batch))
print(desk.total())
desk.take_money(batch)
desk.take_money(Bill(10))
print(desk.total())
desk.inspect()