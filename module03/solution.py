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
    prime_numbers_tofind = 100
    not_prime = [1]
    last_num = 0
    # find the last num to iterate in Sieve of Eratosthenes
    for i in range(0, prime_numbers_tofind):
        if (i * i) <= prime_numbers_tofind:
            last_num = i + 1
    # Generate not prime numbers list
    for x in range(2, last_num):
        for y in range(2, prime_numbers_tofind):
            if x * y not in not_prime:
                not_prime.append(x * y)
                not_prime.sort()
    # Check if numebr is prime
    if num_isprime in not_prime:
        result = False
    else:
        result = True
    return result
is_num_prime = 11
print(f'Is {is_num_prime} a prime: {prime_number(is_num_prime)}')



def fact_digits(num):
    '''Calc sum of factorials of a given num'''
    nums_list = [i for i in str(num)]
    facorial_element_list = []
    for x in nums_list:
        fact = 1
        for y in range(1, int(x)+1): 
            fact = fact * y
        facorial_element_list.append(fact)
    return sum(facorial_element_list)
num_to_calc_fact = 44
print(f'The sum of all single-digit factoriels of {num_to_calc_fact} is: {fact_digits(num_to_calc_fact)}')


def fibonacci(upto_num):
    '''returns a list with the first `upto_num` members of the Fibonacci sequence'''
    fb_list = [1, 1]
    for i in range(2, upto_num):
        fb_next = fb_list[i-2] + fb_list[i-1]
        fb_list.append(fb_next)
    return fb_list
print(fibonacci(6)) # Same as the task in module 2 ???


def fib_number(upto_num):
    '''takes an integer `n` and returns a number, which is formed by concatenating the first `upto_num` Fibonacci numbers'''
    fb_list = [1, 1]
    result = ''
    for i in range(2, upto_num):
        fb_next = fb_list[i-2] + fb_list[i-1]
        fb_list.append(fb_next)
    for z in fb_list:
        result = result + str(z)
    return result
print(fib_number(4))


word_to_test = 'test'
def palindrome(is_palindrome):
    if is_palindrome == ''.join(reversed(is_palindrome)):
        return True
    else:
        return False
print(palindrome(word_to_test))

string_given = 'test'
def char_histogram(string_given):
    '''
    takes a string and returns a dictionary, where each key is a character from `string_given`
    and its value is the number of occurrences of that char in `string_given`
    '''
    list_indexes = []
    # Get chars from string_given
    list_chars = list(set(string_given))
    # Calc char appearance in string_given
    for i in list_chars:
        list_indexes.append(string_given.count(i))
    # Create dictionary from both lists
    result = {k:v for k, v in zip(list_chars, list_indexes)}
    return result
print(char_histogram(string_given))
