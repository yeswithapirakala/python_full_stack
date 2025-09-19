#Abstraction
#Abstraction means hiding the implementation details and showing only the essential features of an object.
#In Python, abstraction is mainly achieved using abstract classes and abstract methods (from the abc module).
#How it works
#Abstract Class → A class that cannot be instantiated directly.
#Abstract Method → A method declared but not implemented in the abstract class.
#Any subclass must provide an implementation of all abstract methods.
#example
from abc import ABC,abstractmethod #abc module -> abstract base class
class shape(ABC):#abstract class
  @abstractmethod
  def area(self):#abstract method
    pass

  @abstractmethod
  def perimeter(self):#abstract method
    pass

class Circle(shape):
  def __init__(self,radius):
    self.radius=radius

  def area(self):
    return 3.14*self.radius*self.radius

  def perimeter(self):
    return 2*3.14*self.radius

c=Circle(5)
print("area:",c.perimeter())
print("perimeter:",c.area())
print("\n")



from abc import ABC, abstractmethod

# Abstract class
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass   # only a definition, no implementation

    @abstractmethod
    def stop(self):
        pass

# Concrete class
class Car(Vehicle):
    def start(self):
        print("Car has started.")

    def stop(self):
        print("Car has stopped.")

class Bike(Vehicle):
    def start(self):
        print("Bike has started.")

    def stop(self):
        print("Bike has stopped.")


# Using abstraction
car = Car()
car.start()
car.stop()

bike = Bike()
bike.start()
bike.stop()
