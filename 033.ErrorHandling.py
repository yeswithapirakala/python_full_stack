
#Introduction to Handling Errors
#An exception is an error that occurs during program execution.
#If not handled, it stops the program

#basic handling of errors
#try, except, finally
try:
  a=int("abc")
except ValueError:
  print("ValueError")

#multiple except blocks
try:
  a=10
  b=0
  c=a/b
except ZeroDivisionError:
  print("ZeroDivisionError")
except ValueError:
  print("ValueError")

print("\n")

#Using else and finally
try:
  num=int("abc")
  print(num)
except ValueError:
  print("ValueError")
else:
  print("no exception you entered a number:",num)
finally:
  print("finally block")

print("\n")

#Raising Your Own Exception
try:
  age = int(input("Enter your age: "))
  if age < 18:
      raise ValueError("You must be 18 or older.")
  print("Access granted.")
except ValueError as e:
  print("Error:", e)


#Example 1: Division by Zero
try:
  a = 10
  b = 0
  result = a / b
  print("Result:", result)
except ZeroDivisionError:
  print("Error: Cannot divide by zero!")



#Example 2: Wrong Input (ValueError)
try:
  num = int(input("Enter a number: "))
  print("You entered:", num)
except ValueError:
  print("Error: Please enter a valid number!")

#Example 3: File Handling Error
try:
  f = open("data.txt", "r")   # file does not exist
  print(f.read())
except FileNotFoundError:
  print("Error: File not found!")

#Example 4: Multiple Exceptions
try:
    x = int("abc")     # ValueError
    y = 10 / 0         # ZeroDivisionError
except ValueError:
    print("Error: Invalid number format!")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

