import math

num_to_sum = -12.3

def sum_of_digits(num):
    sum_all = 0
    mod_num = abs(num)
    split_num = [int(n) for n in str(mod_num) if n.isdigit() == True]
    for i in split_num:
        sum_all = sum_all + i
    return sum_all
print(sum_of_digits(num_to_sum))

def to_digits(num):
    split_num = [int(n) for n in str(num) if n.isdigit() == True]
    return split_num
print(to_digits(1234))

def to_number(num_list):
    num_str = [str(i) for i in num_list]
    result = int(''.join(num_str))
    return result
print(to_number(to_digits(123)))

text_to_test = 'tEsTing some Vowels tExt'

def count_vowels(string_given):
    vowels_list = ['a','e','i','o','u','y']
    vowels_count = 0
    for i in range(len(string_given)):
        if string_given[i].lower() in vowels_list:
            vowels_count = vowels_count + 1
    return vowels_count
print(f'Counted vowels are: {count_vowels(text_to_test)}')

def count_consonants(string_given):
    vowels_list = ['a','e','i','o','u','y']
    consonants_count = 0
    for i in range(len(string_given)):
        if string_given[i].lower() not in vowels_list:
            consonants_count = consonants_count + 1
    return consonants_count
print(f'Counted consonants are: {count_consonants(text_to_test)}')

def prime_number(num_isprime):
    # Set flag - up to where to test
    set_flag = math.sqrt(num_isprime)
    # Generate list with elements to divide on
    list_primers = [i for i in range(2, int(round(set_flag))+1)]
    # Divide to all list numbers up to the flag num and create assessment value for each
    dict_assessments = {i:(True if (num_isprime / i) - (num_isprime // i) == 0 else False) for i in list_primers}
    # Test all the assessmen values (at least one True means False end result)
    if True in dict_assessments.values():
        return False
    else:
        return True

is_num_prime = 18
print(f'Is {is_num_prime} a prime: {prime_number(is_num_prime)}')


'''
def fact_digits(n):
    # Adding a comment to push and create new branch
'''