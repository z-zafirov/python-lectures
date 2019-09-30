class Bill():
    def __init__(self, amount):
        self.amount = amount
        try:
            if amount < 0:
                raise ValueError()
            elif int(amount) * 0 != 0:
                raise TypeError()
        except ValueError('Negative amount provided.'):
            pass
        except TypeError('Non int amount provided.'):
            pass

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

t1 = Bill('a')
print(t1)