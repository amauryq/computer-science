from itertools import count, cycle, product

for c in count(10):
    print(c)
    if c == 19:
        break

for c in cycle('ABCD'): 
    print(c)
    if c == 'D':
        break

for p in product('ABCD', repeat=3): 
    print(p)