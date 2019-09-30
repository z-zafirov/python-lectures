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

t1 = Bill(1.0)
print(t1)
#print(t1.__eq__(t1))