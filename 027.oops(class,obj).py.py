#oops
#object oriented programming
#OOP (Object-Oriented Programming) in Python is a programming paradigm that organizes software design around "objects" rather than "functions and logic." It focuses on creating reusable and modular code through the use of

#class --blueprint of an object
#syntax: class class_name:
#class contains attributes and methods
#attributes--variables
#methods--functions

#object--instance of a class
#syntax: object_name=class_name()
#object _name is any variable name
#object_name.attribute_name
#we can create multiple objects of a class

class student:#class
  school_name="bangtan school"#class variable -tha variable that is defined inside the class but outside the constructor
  def __init__(self,name,age): #constructor--a special member method within a class that automatically runs when an object of that class is created.
    self.name=name#instance variable
    self.age=age#instance variable

#object
s1=student("Hexley",20)
print(s1.name,s1.age)
print(student.school_name,"\n")

#2nd object
s2=student("John",21)
print(s2.name)
s2.name="Doe"
print("updated name of jhon:",s2.name)
print(s2.age,"\n")

#example 2
class Car:
  # constructor
  def __init__(self, brand, color):
      self.brand = brand
      self.color = color

  # instance method
  def display(self):
      print(f"Car Brand: {self.brand}, Color: {self.color}")

# create objects
c1 = Car("Tesla", "Red")
c2 = Car("BMW", "Black")

# call methods
c1.display()
c2.display()
