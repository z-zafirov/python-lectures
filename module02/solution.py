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

pancake_ingredients = {'flour':2, 'eggs':4, 'milk':200, 'butter':False, 'salt':0.001}
test_ingr = 'butter'

def ingredient_exists(ingr, dict):
    ingr_list = dict.keys()
    if ingr in ingr_list:
        return True
    else:
        return False
print(f'Is ingredient {test_ingr} part of teh pancakes receipt: {ingredient_exists(test_ingr, pancake_ingredients)}')

def fatten_pancakes(dict):
    fatten = dict.copy()
    fatten['eggs'] = 6
    fatten['butter'] = True
    return fatten
fatten_receipt = fatten_pancakes(pancake_ingredients)
print(f'Initial ingredient were: \n {pancake_ingredients} \n and after fatten the receipt it is: \n {fatten_receipt}')

def add_sugar(dict):
    ensugar = dict.copy()
    ensugar['sugar'] = 0
    return ensugar
added_sugar = add_sugar(pancake_ingredients)
print(f'Initial ingredient were: \n {pancake_ingredients} \n and after adding sugar it is: \n {added_sugar}')

def remove_salt(dict):
    copied_dict = dict.copy()
    rem_salt = {k: copied_dict[k] for k in copied_dict.keys() - {'salt'}}
    return rem_salt # Returning object address instead of dictionary values...
removed_salt = remove_salt(pancake_ingredients)
print(f'Initial ingredient were: \n {pancake_ingredients} \n and after adding sugar it is: \n {remove_salt}')

def Fibonacci_numbers():
    fb_list = [1, 1]
    result = ''
    for i in range(2, 12):
        fb_next = fb_list[i-2] + fb_list[i-1]
        fb_list.append(fb_next)
    result = str(fb_list)
    return result
print(f'The Fibonacci list for \'12\' elements is: {Fibonacci_numbers()}')