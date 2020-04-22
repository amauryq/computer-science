# Sorting

## Key Functions

Both list.sort() and sorted() have a key parameter to specify a function to be called on each list element prior to making comparisons.

## Using Functions

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

## Using Objects

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

## Operator Module Functions

Python provides convenience functions to make accessor functions easier and faster. The operator module has itemgetter(), attrgetter(), and a methodcaller() function.
Using those functions, the above examples become simpler and faster:

```python
from operator import itemgetter, attrgetter

sorted(student_tuples, key=itemgetter(2))

>>> output
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

sorted(student_objects, key=attrgetter('age'))

>>> output
('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
```

The operator module functions allow multiple levels of sorting. For example, to sort by grade then by age:

```python
sorted(student_tuples, key=itemgetter(1,2))

>>> output
[('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]

sorted(student_objects, key=attrgetter('grade', 'age'))

>>> output
[('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]
```
