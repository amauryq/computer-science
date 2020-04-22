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

## Sorting

```python
student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]

sorted(student_tuples, key=lambda student: student[2])   # sort by age

>>> output
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
```