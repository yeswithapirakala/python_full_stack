
#Inheritance
#Inheritance allows a class (child/subclass) to acquire properties and methods of another class (parent/superclass).
#Parent class (Base class): Contains common functionality.
#Child class (Derived class): Inherits from the parent and can add or override functionality.

#Single Inheritance
class car:
  def __init__(self,name,model):
    self.name=name
    self.model=model

  def details(self):
    print("name:",self.name,"model:",self.model)

class year(car):
  def __init__(self,name,model,year):
    super().__init__(name,model)
    self.year=year

  def details(self):
      print("name:",self.name,"model:",self.model,"year:",self.year)

c=year("audi","a4",2023)
c.details()
print("\n")

# Multiple Inheritance
class school:
  def __init__(self,name,percentage):
    self.name=name
    self.percentage=percentage

  def show_details(self):
    print("name:",self.name,"percentage:",self.percentage)

class highschool:
  def __init__(self,name,marks):
    self.name=name
    self.marks=marks

  def show_details(self):
    print("name:",self.name,"marks:",self.marks)

class collgeentry(school,highschool):
  def __init__(self,name,percentage,marks):
    super().__init__(name,percentage)    #calls the super class
    self.marks=marks     #adds seperately

  def show_details(self):
    print("name:",self.name,"school percentage:",self.percentage,"highschookmarks:",self.marks)

name=input("enter the name: ").strip()#uses of strip() to remove the spaces
percentage=int(input("enter the percentage:").strip())
marks=int(input("enter the marks:").strip())
if 60<percentage<100 and 49<marks<100:
  g=collegeentry(name,percentage,marks)
  g.show_details()
  print("you are selected for the college")
else:
  print("you are not selected for the college ")
  print("for college entry you need to have 60% and above in school and 49 marks and above in highschool")


#Usage of Super Method with different examples.
#super() in single inheritance
class animal:
  def __init__(self,name):#constructor
    self.name=name#instance variable
    print("animal is created")#print statement
class dog(animal):#inheritance
  def __init__(self,name,breed):#constructor
    super().__init__(name)#super() method --calls the parent class constructor
    self.breed=breed#instance variable
    print("dog is created")#print statement

d=dog("charlie","labrador")#object creation
print(d.name,d.breed)
print("\n")

#super() in method overriding
class person:#parent class
  def show(self):#method
    print("person class")#print statement
class student(person):#child class
  def show(self):#method
    super().show()#super() method --calls the parent class method
    print("student class")#print statement
    print("method overriding")#print statement

s=student()#object creation
s.show()
print("\n")

#super() in multiple inheritance
class A:
  def show(self):
      print("class A")

class B(A):
  def show(self):
      super().show()
      print("class B")

class C(B):
  def show(self):
      super().show()
      print("class C")

c = C()
c.show()
print("\n")

#Multi Level Inheritance-
#When a class inherits from more than one parent class, it’s called multiple inheritance.


#single mullti level inheritance
class father:
  def skills(self):
    print("father :cooking")

class mother:
  def skills(self):
    print("mother :painting")

class child(father,mother):
  def skills(self):
    super().skills()
    print("child class")

c=child()
c.skills()
print("\n")

#calling both parents explicitly
class Father:
  def skills(self):
    print("father:cooking")

class Mother:
  def skills(self):
    print("mother :painting")

class Child(father,mother):
  def skills(self):
    Father.skills(self)
    Mother.skills(self)
    print("child class")

c=Child()
c.skills()
print("\n")

#multiple inheritance  with __init__() method
class A:
  def __init__(self):
    print("A init")

class B:
  def __init__(self):
    print("B init")

class C(A,B):
  def __init__(self):
    super().__init__()
    print("C init")

c=C()
print("\n")

#Method Resolution Order (MRO) demonstration.
#MRO decides the order in which Python looks for methods when multiple inheritance is used.
class A:
  def __init__(self):
    print("A init")

class B(A):
  def __init__(self):
    super().__init__()
    print("B init")

class C(A):
  def __init__(self):
    super().__init__()
    print("C init")
class D(B,C):
  def __init__(self):
    super().__init__()#calls the super class
    print("D init")

d=D()
print("\n")


# Hierarchical Inheritance
#In hierarchical inheritance, one parent class is inherited by multiple child classes.
class Parent:
  def show_parent(self):
    print("Parent class")

class child1(Parent):
  def show_child1(self):
    print("child1 class")

class child2(Parent):
  def show_child2(self):
    print("child2 class")

p=Parent()
c1=child1()
c2=child2()
p.show_parent()
c1.show_child1()
c2.show_child2()
print("\n")


#Hybrid Inheritance.
#Hybrid inheritance is a combination of two or more types of inheritance.
#Hybrid inheritance = combination of two or more types of inheritance (single, multiple, multilevel, hierarchical).
class animal:
  def sound(self):
    print("animal sound")

class dog(animal):#single inheritance
  def sound(self):
    print("dog bark")

class cat(animal):#hierarchical inheritance
  def sound(self):
    print("cat meow")

class pet(dog,cat):#multiple inheritance
  def sound(self):
    print("pet sound")

pet=pet()
pet.sound()
print("\n")