#instance methods
#instance methods are the methods that are defined inside the class and are used to access the instance variables of the class.
#instance methods are called using the object of the class.
#instance methods can access the instance variables and class variables.
#instance methods can modify the instance variables and class variables.
class student:
  school_name = "bangtan school"

  def __init__(self, name, age):
    self.name = name
    self.age = age

  #instance method
  def change_name(self, new_name):
    self.school_name = new_name
    print(f"school name changed to {self.school_name}")


#object
s1 = student("harry", 26)  #constructor called
print(s1.name, s1.age)
print(student.school_name)
s1.change_name("Purple Heart Academy")  #instance method called
#why s1.change_name why not student.change_name?
#we use s1.change_name because it’s an instance method that needs an object (self) to work on.If you want to change the school name for the whole class, you should use a class method instead.
print(student.school_name, "\n")


#class methods
#class methods are the methods that are defined inside the class and are used to access the class variables of the class.
#class methods are called using the class name.
class student:
  school_name = "bangtan school"

  def __init__(self, name, age):
    self.name = name
    self.age = age

  #class method
  @classmethod
  def change_school_name(
      cls, new_name
  ):  #cIn a class method, the first parameter is cls, which represents the class itself (just like self represents the object in an instance method). cls is not a keyword—you could technically name it anything—but by convention, we use cls.
    cls.school_name = new_name
    print(f"school name changed to {cls.school_name} \n")

  #instance method
  def display(self):
    return f"name:{self.name},age:{self.age}"


#object
s1 = student("jeon", 26)
print(s1.display())
print(f"before changing: {student.school_name} ")
student.change_school_name("Purple Heart Academy")

#static methods
#A static method is a method inside a class that does not depend on either the instance (self) or the class (cls).
#It behaves just like a regular function, but it’s placed inside a class for better organization.
#Defined with the @staticmethod decorator.


class student:
  school_name = "bangtan school"

  def __init__(self, name, age):
    self.name = name
    self.age = age

  #static method
  @staticmethod
  def change_school_name(new_name):
    school_name = new_name
    print(f"school name changed to {school_name}")


#object
s1 = student("tae", 27)
print(s1.name, s1.age)
print(student.school_name)
student.change_school_name("Purple Heart Academy")










