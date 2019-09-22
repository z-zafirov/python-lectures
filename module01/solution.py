'''
* Create a program named `solution.py`
* Define a function with the following signature `def f_c(X)` which
  returns the constant 4 for any input parameter.
* Document what the function `f_c` does
* Write a function `f_x(x, a, b)` which implements the formula `f(x) = a*x + b`!
* Write a function `sum(x)` which returns the sum of `f_x()` called 3 times with
  parameters `x, 1, 1`, `x, 2, 2`, `x, 3, 3`!
'''

x = 1
def  f_c(x):
    '''
    Fc returns always 4 no matter what x parameter you provide to it
    '''
    return 4
print(f'Fc(x) will always return \'{f_c(x)}\' no matter of param provided (e.g. x={x})')


a = 1
b = 2
def f_x(x, a, b):
    '''
    Fc calculates `f(x) = a*x+b`
    '''
    return a*x+b
print(f'Fx(a*x+b) for x={x}, a={a} and b={b} returns: {f_x(x,a,b)}')


def sum(x):
    # sum(x, a, b) where x, a and b are the results of Fx(x,a,b) for number of 'runs'
    to_sum = [f_x(x, i, i) for i in range(1,4)]
    z = 0
    for y in range(len(to_sum)):
        z = z + to_sum[y]
    return z
print(f'The sum of {4-1} Fx() runs is: {sum(x)}')