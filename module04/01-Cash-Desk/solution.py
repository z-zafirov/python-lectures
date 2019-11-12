class Bill():

    def __init__(self, amount):
        self.amount = amount
        if amount * 0 != 0 or amount % 1 != 0:
            raise TypeError('Non-int amount provided.')
        elif amount < 0:
            raise ValueError('Negative amount provided.')        

    def __int__(self):
        return int(self.amount)

    def __str__(self):
        return str(f'A {self.amount}$ bill')
    
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
            x = x + int(i)
        return x

'''
b1 = int(Bill(2))
list_bills = [b1, 5, 10, 20, 50]
bb1 = BatchBill(list_bills)
print(bb1.__len__())
print(bb1.total())
'''

class CashDesk():
    def __init__(self):
        self.cash_desk = {}

    def take_money(self, money): # take_money is to initiate CashDesk object!
        ''' where `money` can be either `Bill` or `BatchBill` class '''
        if isinstance(money, int) or isinstance(money, Bill):          # if money is int or Bill
            self.money = [int(money)]
        elif isinstance(money, list) or isinstance(money, BatchBill):  # if money is list or BatchBill
            self.money = [int(y) for y in money]
        # remove bills from the cash_desk if there are available of that value
        for m in self.money:
            if m in self.cash_desk.keys():
                self.cash_desk[m] = self.cash_desk[m] + 1
            else:
                self.cash_desk[m] = 1

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
        inspect_text =  """We have a total of 40$ in the desk
We have the following count of bills, sorted in ascending order:"""

        for i in range(len(self.cash_desk)):
            count = list(self.cash_desk.values())[i]
            value = list(self.cash_desk.keys())[i]
            inspect_text = ''.join(f'{value}$ bills - {count}\n')
            #print(f'{value}$ bills - {count}')
        return inspect_text

'''
values = [10, 20, 50, 100, 100, 100]
bills = [Bill(value) for value in values]
batch = BatchBill(bills)
desk = CashDesk()
#'''
'''
print(desk.total())                                    # 0
desk.take_money(50)                                    # +50
desk.take_money([50, 20])                              # +70
desk.take_money(Bill(10))                              # +10
desk.take_money([Bill(10), (Bill(20))])                # +30
desk.take_money(BatchBill([10, 20]))                   # +30
desk.take_money(BatchBill([(Bill(10)), Bill(20)]))     # +30
print(desk.total())                                    # 220
#'''
'''
print(desk.total())                                    # 860
desk.take_money(batch)                                 # -380
desk.take_money(Bill(10))                              # -10
print(desk.total())                                    # 470
desk.inspect()
#'''