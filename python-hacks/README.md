# PyTricks

## Python's list comprehensions are awesome

```python
vals = [expression 
        for value in collection 
        if condition]

# This is equivalent to:

vals = []
for value in collection:
    if condition:
        vals.append(expression)

# Example:

>>> even_squares = [x * x for x in range(10) if not x % 2]
>>> even_squares
[0, 4, 16, 36, 64]
```

## Build a matrix

```python
>>> columns = 3
>>> rows = 2
>>> grid = [[0 for _ in range(columns)] for _ in range(rows)]
[[0, 0, 0], [0, 0, 0]]
```

## Working with enumerates

```python
>>>[tup for tup in enumerate([1, 2, 3], start=10)]
[(10, 1), (11, 2), (12, 3)]
```

## Working with map, filter, reduce and lambda

```python
>>>l = [1, 2, 3, 4]
>>>list(map(lambda x: x*x, l))
>>>list(filter(lambda x: x % 2 == 0, l))
```

## Arguments types

1.Positional arguments that are passed positionally
2.Keyword arguments that are supplied by keywords

```python
def my_func(a, b, /, c, d, *, e, f):
    return a+b+c+d+e+f
  
my_func(1,2,3,4,5,6)          # invalid as e and f are keyword-only
my_func(a=1,b=2,3,4,e=5,f=6)  # invalid as a and b are position-only
my_func(1,2,3,d=4,e=5,f=6)    # returns 21
my_func(1,2,c=3,d=4,e=5,f=6)  # returns 21
```
