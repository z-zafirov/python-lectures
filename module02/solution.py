'''
* Implement a function `num_add(a, b)` which adds two numbers together
* Implement a function `num_sub(a, b)` which subtracts two numbers
* Implement a function `num_mul(a, b)` which multiplies two numbers
* Implement a function `num_div(a, b)` which divides the two numbers
* Implement a function `num_floor(a, b)` which implements floor division
* Implement a function `num_rem(a, b)` which implements remainder division
'''

a = 7
b = 2
def num_add(a, b):
    return a + b
print(f'For a={a} and b={b} : a + b = {num_add(a,b)}')

def num_sub(a, b):
    return a - b
print(f'For a={a} and b={b} : a - b = {num_sub(a,b)}')

def num_mul(a, b):
    return a * b
print(f'For a={a} and b={b} : a * b = {num_mul(a,b)}')

def num_div(a, b):
    return a / b
print(f'For a={a} and b={b} : a / b = {num_div(a,b)}')

def num_floor(a, b):
    return a // b
print(f'For a={a} and b={b} : a // b = {num_floor(a,b)}')

def num_rem(a, b):
    return a % b
print(f'For a={a} and b={b} : a % b = {num_rem(a,b)}')


is_true = True
is_false = False

def ingredient_exists(ingr, dict_data):
    ingr_list = dict_data.keys()
    if ingr in ingr_list:
        return True
    else:
        return False

def fatten_pancakes(dict_data):
    fatten = dict_data.copy()
    fatten['eggs'] = 6
    fatten['butter'] = True
    return fatten

def add_sugar(dict_data):
    ensugar = dict_data.copy()
    ensugar['sugar'] = 0
    return ensugar

def remove_salt(dict_data):
    rem_salt = dict_data.copy()
    del rem_salt['salt']
    return rem_salt

pancake_ingredients = {'flour':2, 'eggs':4, 'milk':200, 'butter':False, 'salt':0.001}
test_ingr = 'butter'

print(f'\nIs ingredient \'{test_ingr}\' part of the pancakes receipt: {ingredient_exists(test_ingr, pancake_ingredients)}\n')
print(f'>_The initial ingredients list is: {pancake_ingredients}')
print(f'_after fatten-receipt the list is: {fatten_pancakes(pancake_ingredients)}')
print(f'___after adding sugar the list is: {add_sugar(pancake_ingredients)}')
print(f'_____and_after removing \'salt\' is: {remove_salt(pancake_ingredients)}')
print(f'Note: All changes are done over a copy of the initial dict!')


def fibonacci_numbers(upto_num):
    fb_list = [1, 1]
    for i in range(2, upto_num):
        fb_next = fb_list[i-2] + fb_list[i-1]
        fb_list.append(fb_next)
    return fb_list

def add_fibonacci(list_data):
    '''
    adds the next Fibonacci number to the provided list of elements (here is result of the call to fibonacci_numbers(12))
    '''
    list_data.append(list_data[len(list_data)-2] + list_data[len(list_data)-1])
    return list_data

def fib_exists(list_data, ifnum_exist):
    if ifnum_exist in list_data:
        result = True
    else:
        result = False
    return result

fibonacci12 = fibonacci_numbers(12)
fibonacci13 = add_fibonacci(fibonacci_numbers(12))
fbn_lookup_num = 1

def which_fib(list_data, fbn_num_index): # The test result is not-thrown ValueError exception, probably fot the list_data!?
    try:
        if fib_exists(list_data, fbn_num_index) == True:
            result = list_data.index(fbn_num_index)+1 # Because counting from 1
        else:
            raise ValueError
    except ValueError:
        result = f'Provided number {fbn_num_index} does not exist in the Fibonacci list with 12 elements.'
    return result

print(f'\nThe Fibonacci list for \'12\' elements is: {fibonacci12}')
print(f'_and when added one more (Fibonacci 13): {fibonacci13}')
print(f'\nDoes \'{fbn_lookup_num}\' exist in Fibonacci(13): {fib_exists(fibonacci13, fbn_lookup_num)}')
print(f'\nIndex lookup for \'{fbn_lookup_num}\' in Fibonacci(12) result: {which_fib(fibonacci12, fbn_lookup_num)}')