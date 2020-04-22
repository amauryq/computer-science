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

### Key Functions

Both list.sort() and sorted() have a key parameter to specify a function to be called on each list element prior to making comparisons.

### Using Functions

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

### Using Objects

```python
class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age
    def __repr__(self):
        return repr((self.name, self.grade, self.age))
        
student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]

sorted(student_objects, key=lambda student: student.age)   # sort by age

>>> output
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]        
```