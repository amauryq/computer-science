# String Formatting

## Styles

```python
'Hello %s' % name    # C-style

'My name is {1}, {0} {1}'.format('James', 'Bond')  # Added in Python 3.0

f'I am {age} years old'  # f-string added in Python 3.6
```

## Samples

```python
>>> first = 'James'
>>> last = 'Bond'
>>> age = 90
>>> message = 'No, Mr. %s, I expect you to die' % last
>>> print(message)
No, Mr. Bond, I expect you to die
>>> print('The name is %s, %s %s' % (last, first, last))
The names is Bond, James Bond
>>> print('Sean Connery is now %d years old' % age)
Sean Connery is now 90 years old
>>> print('pi: %f \nshort pi %0.2f' % (math.pi, math.pi))
pi: 3.141593
short pi 3.14
>>> message = f'No, Mr. {last}, I expect you to die'
>>> print(message)
No, Mr. Bond, I expect you to die
>>> print(f'The name is {last}, {first} {last}')
The name is Bond, James Bond
>>> print(f"Sean's age times pi is {age*math.pi}")
Sean's age times pi is 282.7433388230814
>>> print(f"Sean's age times pi is {age*math.pi:.2f}")
Sean's age times pi is 282.74
```

## sep, end, and flush

```python
>>> print('There are', 6, 'members of Monty Python')
There are 6 members of Monty Python
>>> message = 'There are' + 6 + 'members of Monty Python'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> message = 'There are' + str(6) + 'members of Monty Python'
>>> print(message)
There are6members of Monty Python
>>> print('There are', 6, 'members of Monty Python', sep='😀')
There are😀6😀members of Monty Python
>>> print('There are', 6, 'members of Monty Python', sep=' ')
There are 6 members of Monty Python
>>> print('There are', 6, 'members of Monty Python', sep=None)
There are 6 members of Monty Python
>>> print('There are', 6, 'members of Monty Python', sep='')
There are6members of Monty Python
>>> print('There are', 6, 'members of Monty Python', sep='\n')
There are
6
members of Monty Python
>>> data = [ 
...     ['year', 'last', 'first'], 
...     [1943, 'Idle', 'Eric'], 
...     [1939, 'Cleese', 'John'] 
... ]
>>> for row in data:
...     print(*row, sep=',')
... 
year,last,first
1943,Idle,Eric
1939,Cleese,John
```

## Simulate Counting

```python
import time

def count_items(items):
    print('Counting ', end='', flush=True)
    num = 0
    for item in items:
        num += 1
        time.sleep(1)
        print('.', end='', flush=True)

    print(f'\nThere were {num} items')
```

## Sound

```python
print('one', 'two', 'three', 'four', sep='\a')
```
