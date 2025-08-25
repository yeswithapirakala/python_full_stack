#modules
#A module is just a Python file (.py) that contains code

#Built-in Modules (already provided by Python)
#Example: math, os, sys, random, etc.
import random

#random method returns value between the range 0.0 to 1.0
#randint method returns random integer between the range a and b inclusive
#choice[seq]  it randomly returns an element from the non empty sequence
#choices(seq,k) it randomly returns k sized list of elements chosen from the sequence)
print(random.random(),"\n")
print(random.randint(1,6),"\n") 
print(random.randrange(9,99,3),"\n")
print(random.choices([1,2,3,'a','b','c'],k = 2),"\n")
sl=[1,2,3,'a','b','c']
random.shuffle(sl)
print(sl,"\n") 



#sys
import sys 

#getsizeof() method returns the size of an object in bytes
#version returns the version of python
#executable returns the path to the python interpreter(p)
#exit()  stop execution of the program
#sys.platform returns the platform  current opersting system

print(sys.version,"\n")
print(sys.getsizeof(10),"\n")
print(sys.getsizeof(10.0),"\n")
print(sys.getsizeof('yeswitha'),"\n")
print(sys.getsizeof([]),"\n")
print(sys.getsizeof(()),"\n")
print(sys.executable, "\n")
print(sys.platform,"\n")
"""sys.exit()
print("you are done")"""

#math

import math
print(math.factorial(5),"\n")
print(math.sqrt(16),"\n")
print(math.ceil(5.6),"\n")
print(math.floor(535.6),"\n")
print(math.trunk(535.6),"\n")

#User-defined Modules (files you create with your own functions/classes).
#User-defined Modules (files you create with your own functions/classes).
import add
import sub
import mul
import div
import mod

while True:
  choice=int(input("enter the operation 1.add 2.sub 3.mul 4.div 5.mod 6.exit :"))
  if choice == 1:
    n = list(map(int, input("input:").split())) 
    res = add.addition(*n)
    print(res ,"\n")
  elif choice == 2:
    a,b=map(int,input("a,b input:").split())
    res = sub.substraction(a,b)
    print(res ,"\n")
  elif choice ==3:
    n = list(map(int, input("input:").split())) 
    res = mul.multiply(*n)
    print(res)
  elif choice == 4:
    a,b=map(int,input("a,b input:").split())
    res = div.divide(a,b)
    print(res ,"\n")
  elif choice == 5:
    a,b=map(int,input("a,b input:").split())
    res = mod.moduls(a,b)
    print(res ,"\n")
  elif choice == 6:
    print("exit")
    break
  else:
    print("invalid choice")
    print("please enter a valid choice between 1 to 6")
    break

#add.py,sub.py,mul.py,div.py,mod.py
#Third-party Modules (installed using pip, e.g., numpy, pandas, flask).

