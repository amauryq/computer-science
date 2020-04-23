# run with
# python -m doctest fizz_buzz.py
#
def fizz_buzz(numbers):
    '''
    Given a list of integers:
    1. Replace all integers that are divisible by 3 with "fizz"
    2. Replace all integers that are divisible by 5 with "buzz"
    3. Replace all integers that are divisible by 3 and 5 with "fizzbuzz"
    >>> numbers = [45, 22,14, 65, 97, 72]
    >>> fizz_buzz(numbers)
    >>> numbers
    ['fizzbuzz', 22, 14, 'buzz', 97, 'fizz']
    '''
    for i, num in enumerate(numbers):
        num = numbers[i]
        if num % 3 == 0:
            numbers[i] = 'fizz'
        if num % 5 == 0:
            numbers[i] = 'buzz'
        if num % 3 == 0 and num % 5 == 0:
            numbers[i] = 'fizzbuzz'
