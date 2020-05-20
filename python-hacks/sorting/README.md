# Sorting

## Key Functions

Both list.sort() and sorted() have a key parameter to specify a function to be called on each list element prior to making comparisons.

## Using Functions

```python
>>>student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
>>>sorted(student_tuples, key=lambda student: student[2])   # sort by age
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
```

## Using Dictionaries

```python
>>>animals = [
    { 'type': 'dog', 'name': 'Stephanie', 'age': 8},
    { 'type': 'dog', 'name': 'Devon', 'age': 3},
    { 'type': 'rhino', 'name': 'Moe', 'age': 8}
]

>>> sorted(animals, key=lambda animal: animal['age'])
[{'type': 'dog', 'name': 'Devon', 'age': 3}, {'type': 'dog', 'name': 'Stephanie', 'age': 8}, {'type': 'rhino', 'name': 'Moe', 'age': 8}]
```
## Using Objects

```python
>>>class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age
    def __repr__(self):
        return repr((self.name, self.grade, self.age))
        
>>>student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]

>>>sorted(student_objects, key=lambda student: student.age)   # sort by age
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]        
```

## Operator Module Functions

Python provides convenience functions to make accessor functions easier and faster. The operator module has itemgetter(), attrgetter(), and a methodcaller() function.
Using those functions, the above examples become simpler and faster:

```python
from operator import itemgetter, attrgetter

>>>sorted(student_tuples, key=itemgetter(2))
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

>>>sorted(student_objects, key=attrgetter('age'))
('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
```

The operator module functions allow multiple levels of sorting. For example, to sort by grade then by age:

```python
>>>sorted(student_tuples, key=itemgetter(1,2))
[('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]

>>>sorted(student_objects, key=attrgetter('grade', 'age'))
[('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]
```
## Exiting/Terminating Python Scripts

```python
# Register an exit
import atexit
 
atexit.register(print,"Program exited successfully!")
name=input("What's your name?\n")
print("Hi,",name,"!")

# Releasing resources
import atexit
 
file=open("testfile.txt","w")
file.write("let's write some text!\n")
atexit.register(file.close)

# Exit after a time
import time
import sys
from multiprocessing import Process

integer=sys.argv[1]
init=map(int, integer.strip('[]')) 
num=list(init)[0]

def exclaim(int): 
    time.sleep(int)
    print("You were very patient!")
 
if __name__ == '__main__':
    program = Process(target=exclaim, args=(num,))
    program.start()
    program.join(timeout=5)
    program.terminate()

# Exiting using a return statement
import time
import sys

def stop(isTrue): 
    for a in range(0,1):
        if isTrue:
            break
        else:
            print("You didn't want to break!")
            return sys.exit()
 
mybool = False
stop(mybool)
print("You used break!")

# Exit on keypress
import time
 
try:
    i=0
    while 1==1:
        i=i+1
        print(i)
        time.sleep(1)
except KeyboardInterrupt:
    print("\nWhoops I took too long")
    raise SystemExit

# Exit a multithreaded program
import threading
import os
import sys
import time
 
integer=sys.argv[1]
init=map(int, integer.strip('[]'))
num=list(init)[0]
 
def exclaim(int):
    time.sleep(int)
    os._exit(1)
    print("You were very patient!")
 
if __name__ == '__main__':
    program = threading.Thread(target=exclaim, args=(num,))
    program.start()
    program.join()
    print("This should print before the main thread terminates!")

# Exit a multithreaded program - Preferred Method
import threading
import os
import sys
import time
import atexit
 
integer=sys.argv[1]
init=map(int, integer.strip('[]'))
num=list(init)[0]

atexit.register(print,"Threads exited successfully!")

def exclaim(int):
    time.sleep(int)
    print("You were very patient!")
 
if __name__ == '__main__':
    program = threading.Thread(target=exclaim, args=(num,))
    program.start()
    program.join()

# End without sys exit
class MyException(Exception):
    pass
try:
    raise MyException()
except MyException:
    print("The exception works!")

    import atexit 
 
# Exit and restart
$ nano restart.py
import os
import atexit

atexit.register(os.system, "python3 restart.py")
 
try: 
    n=0
    while 1==1:
        n=n+1
        if n%5==0:
            raise SystemExit
except:
    print("Exception raised!")
```
