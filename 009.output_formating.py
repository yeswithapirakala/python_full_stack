#output formatting

#using old style formating[using commas]
#basic
n = "hexley"
age = 22
print("name", n, "age", age, "\n")

#numbers
a = 10
b = 20
print("a is :", a, "b is :", b, "and the sum", a + b, "\n")

#different data types
na = "hexley"
age = 22
passed = True
print("name:", na, "age:", age, "passed:", passed, "\n")

#using modulo operator
#basic
n = "hexley"
age = 22
print("name %s age %d \n" % (n, age))

#float formating
pi = 3.141592653589793
print("value of pi is  %.2f" % pi, "\n")

#multiple datatypes
name = "hexley"
score = 9.8
passed = True
print("name : %s score : %.2f passed : %s \n" % (name, score, passed), "\n")

#fstring
#basic
name = "hexley"
age = 22
print(f"name : {name} age : {age} ", "\n")

#float formating
pi = 3.141592653589793
print(f"value pf pi is {pi:.2f}", "\n")

#inline calculations
a = 10
b = 20
print(f"a is {a} b is {b} and the sum is {a+b}", "\n")

#allignamt and width
na = "hexley"
age = 22
print(f"|{'name':10}|{'age':5}|")
print(f"|{na:10}|{age:5}|", "\n")

#expression using f string
age = 22
print(f"Next year, I will be {age + 1} years old.", "\n")


#using string
def greet(user):
  return f"hello {user} ! \n"


print(greet("charlie"))

#using dot fromat method(.format()))
#positional formating
name = "yeswitha"
age = 22
print("name : {} and age : {}".format(name, age), "\n")

#positional indexes
na = "pirakala"
age = 22
print("name : {0} and age : {1}".format(na, age), "\n")

#named placehlders
print("name : {n} and age : {a}".format(n="hexley", a=22), "\n")

#float formatting
pi = 3.141592653589793
print("pi is {:.2f}".format(pi), "\n")

#alignment and width
na = "charlie"
age = 8
print("{:<10} |{:>5}".format("name", "age"), "\n")
print("{:<10} |{:>5}".format(na, age), "\n")

#dictonary
student = {"name": "David", "grade": 92}
print("Student: {name}, Grade: {grade}".format(**student))
