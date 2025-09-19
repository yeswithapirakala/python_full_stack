#polymorphism
#same function name but different functionality
#one operation can perform different actions based on operands
#same funtition for multiple input,operations

"""
we can achive polymorphism in 
1.operators- -,+,*,/
2.methods -method overloading(class),method overriding(through inheritance)
3.functions - len() """

#####operator overloading#########
#-same operator for different operations
#the basic math operators(+,*) can act as numeric operators if operands is integers as well as string operators if the operanda are strings
#the + operator can act as numeric addition as well as string concatenation


#polymorphism through functions
#the len() function can be used to find the length of a string, list, tuple, dictionary, set, etc.
print(len({1,2,1,2}),"\n")
print(len((0,1)),"\n")
print([1,2,3,4,5,6,7,8,9,10],"\n")
print(len("python"),"\n")

#2.methods -method overloading(class),method overriding(through inheritance
#method overriding- a child class heving same method as same as its parent calss method name
#if you call that method with child object, then child class method will overrides the parent class method
class Parent():
  def show(self):
    print("Parent class method \n")
class child(Parent):
  def show(self):
    print("child class method \n")
p=Parent()
c=child()
p.show()
c.show()
#child class show method overrides the parent class show method

#if you wnat to execute the parent class method we need to use super method
#to avoid method overriding we use super() function
class parent():
  def show(self):
    print("Parent class method \n")
class child(parent):
  def show(self):
    super().show() # to avoid method overriding we use super() function
    print("child class method \n")
p=Parent()
c=child()
p.show()
c.show()

#method overloading
#one class have multiple methods with same name but different parameters
#in this case last defined method overrides the previous methods
#in python method overloading is not possible because python does not support method overloading
#in python we can achive method overloading by using default arguments, *args, **kwargs
class math:
  def add(self,a,b):
    return a+b
  def add(self,a,b,c):
    return a+b+c
  def add(self,a,b,c,d):
    return a+b+c+d
m=math()
print(m.add(10,20,2,3),"\n")
"""print(m.add(2,3,4))
print(m.add(5,10))"""

#  through default arguments
class math:
  def add(self,a,b,c=0,d=0):
    return a+b+c+d
m=math()
print(m.add(10,20,2,3),"\n")
print(m.add(2,3,4),"\n")
print(m.add(5,10),"\n")