#Encapsulation.
#Data Hiding → Prevents outside classes from directly modifying sensitive data.
#Controlled Access → Data can only be accessed/modified through methods.
#Security → Protects object’s integrity.
#Flexibility → Internal implementation can change, but external code won’t break.
account_details = {123456789: {"balance": 100000, "pin": 1234}}

class BankAccount:
    def __init__(self, account_no, balance, pin):
        self.account_no = account_no  # public
        self.balance = balance        # public
        self.__pin = pin              # private

    def check_login(self, account_no, pin):
        if account_no in account_details:
            if account_details[account_no]["pin"] == pin:
                print("Login success")
            else:
                print("Incorrect pin. Login failed.")
        else:
            print("Account number not found. Login failed.")

    def show_details(self):
        print("Account No:", self.account_no, "Balance:", self.balance)

# Input
account_no = int(input("Enter the account number: "))
pin = int(input("Enter the pin: "))

# Fetch balance from the dictionary
if account_no in account_details:
    balance = account_details[account_no]["balance"]
    # Create object
    b = BankAccount(account_no, balance, pin)
    b.check_login(account_no, pin)
    b.show_details()
else:
    print("Account number not found.")



# Access Specifiers
#access specifiers are also called the access modifiers.
#define how the members(variables,methods) of the class can be accessed from outside the class
#In Python, there are no strict access specifiers like in Java or C++, but we follow naming conventions to indicate the level of access:

#public: accessible from anywhere
class student:
  def __init__(self,name,age,salary):
    self.name=name
    self.age=age
    self.salary=30000
s1=student("hexley",21,100000)
print(s1.name,s1.age,s1.salary,"\n")



#protected:deined by _ before the variable name
#protected - attributes is accessible within the class and subcalsses
class student:
  def __init__(self,name,age,salary):
    self.name=name
    self.age=age
    self._salary=30000 #protected variable
  def details(self):
    print("name:",self.name,"salary:",self._salary )#printed within the class
s1=student("hexley",21,100000)
s1.details()
print("\n")

#using subclass
class Emp:
  def __init__(self, name, age, salary):
      self.name = name
      self.age = age
      self._salary = salary   # take salary from argument, not fixed 30000

class Details(Emp):
  def display(self):
      print("Name:", self.name, "Salary:", self._salary)  # accessed in subclass

s1 = Details("jeon", 21, 100000)
s1.display()
print(s1.name)   # public attribute, can access directly
print("\n")


#private:defined by __ before the variable name
#private is accessible only within the class only
class attendance:
  def __init__(self,name,rollno,attendance):
    self.name=name
    self.rollno=rollno
    self.__attendance=attendance
  def details(self):
    print("name:",self.name,"rollno:",self.rollno,"attendance:",self.__attendance)  
a=attendance("hexley",21,95)
a.details()
print(a.name,a.rollno)
print()


