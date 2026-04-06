'''Debugging in python
Bug--->Error 

Types of Errors:

Syntax Errors -->Missing of colon,Missing of Identation -->
Runtime Errors -->Division of any num with Zero 
Logical Errors -->Missing of logics

Debugging Techniques:
print() --> run the code line by line 
try - except 
Using of pdb 

pdb commands:
1)n-->to get output in next line
2)p variable -->to get value of variable
3)l-->list nearby code
4)c-->continue the execution of code
5)s-->start the function
 

try: 
    a=int(input("Enter a number:"))
    print(10/a)
except ZeroDivisionError:
    print("Can not divisible by zero")
except ValueError:
    print("Invalid Input") 
'''

import pdb
def add(a,b):
    pdb.set_trace()
    return a+b 
a=int(input("Enter a:"))
b=int(input("Enter b:"))
print(add(a,b)) 


