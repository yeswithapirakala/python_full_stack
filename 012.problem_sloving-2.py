#number is positive or negative or zero even or odd
num = 0
if num > 0:
  print(f"{num} is positive", "\n")
  if num % 2 == 0:
    print(f"{num} is even", "\n")
  else:
    print(f"{num} is odd", "\n")
elif num < 0:
  print(f"{num} is negative", "\n")
else:
  print(f"{num} is zero", "\n")

#assign grades based on marks
#90+:A+,80-89:A,70-79:B,60-69:C,50-59:D,<50:F
m = 46
if m >= 90:
  print("A+", "\n")
elif m > 89 and m < 80:
  print("A", "\n")
elif m > 79 and m < 70:
  print("B", "\n")
elif m > 69 and m < 60:
  print("C", "\n")
elif m > 59 and m < 50:
  print("D", "\n")
else:
  print("fail", "\n")

#simple calculator using +,-,*,/,%
"""a,b =map(int,input("enter the a,b :").split())
op=input("enter the operator(+,-,*,/,%) : ")
print(a,b,op)
if op=="+":
  print(a+b,"\n")
elif op=="-":
  print(a-b,"\n")
elif op=="*":
  print(a*b,"\n")
elif op=="/":
  print(a/b,"\n")
else:
  print("invalid operator","\n")

# Check whether a triangle is valid based on the sum of its angles.
x,y,z=map(int,input("enter the x,y,z :"). split())
if x+y+z==180:
  print("triangle is valid","\n")
else:
  print("traingle is invalid","\n")"""

#num is divisible by 3 and 5
n = 15
if num % 3 == 0 and num % 5 == 0:
  print("num is divisible by 3 and 5", "\n")
else:
  print("num is not divisible by 3 and 5", "\n")

#determine if thr number is a three digit number or not
n = 123
if 99 < n < 1000:
  print("num is three digit number", "\n")
else:
  print("num is not three digit number", "\n")

# Check if a day number (1-31) corresponds to day.
day = 35
if 1 <= day <= 31:
  print("day is valid", "\n")
else:
  print("day is invalid", "\n")

#Check if a number is even and multiple of 7.
num = 5
if num % 2 == 0 and num % 7 == 0:
  print("num is even and multiple of 7", "\n")
elif num % 2 != 0 and num % 7 == 0:
  print("num is not even but multiple of 7", "\n")
elif num % 2 == 0 and num % 7 != 0:
  print("num is even but not multiple of 7", "\n")
else:
  print("num is not even and not multiple of 7", "\n")


#Determine the type of triangle (Equilateral, Isosceles, Scalene) using sides.
g, h, i = 5, 5, 3
if g == h == i:
  print("Equilateral", "\n")
elif g == h or h == i or i == g:
  print("Isosceles", "\n")
else:
  print("Scalene", "\n")

#Calculate electricity bill slab-wise rates.
"""Units Consumed	Rate per Unit
0 – 100 units	₹1.5
101 – 200 units	₹2.5
201 – 300 units	₹4.0
Above 300 units	₹6.0"""

unit = 330
if unit >= 0 and unit <= 100:
  print(unit * 1.5, "\n")
elif unit >= 101 and unit <= 200:
  print(unit * 2.5, "\n")
elif unit >= 201 and unit <= 300:
  print(unit * 4.0, "\n")
else:
  print(unit * 6.0, "\n")

#Check if a number is within a range (e.g., 50-100). 50 <= num <= 100:
num = 101
if 50 <= num <= 100:
  print("num is within the range", "\n")
else:
  print("num is not within the range", "\n")

#Check whether a given year is a century year.
year = 2025
if year % 100 == 0:
  print(year // 100, "st century year", "\n")
else:
  print((year // 100) + 1, "st century year", "\n")

#Compare two numbers and display the greater and the difference.
o, p = 20, 10
if o > p:
  print(o, "is greater", "\n")
  print(o - p, "is difference", "\n")
else:
  print("o is not greater", "\n")

#Check if a day number (1-7) corresponds to weekday or weekend.
day = 6
if 1 <= day <= 5:
  print(f"{day} is weekday", "\n")
else:
  print(f"{day} is weekend", "\n")

#Check if three angles can form a right-angled triangle.
x, y, z = 90, 70, 20
if x + y + z == 180:
  print("triangle is valid", "\n")
else:
  print("triangle is invalid", "\n")

#check if three sides can form a right angled triangle.
a,b,c=2,2,3
if a**2+b**2==c**2:
  print("triangle is right angled","\n")
elif b**2+c**2==a**2:
  print("triangle is right angled","\n")
elif c**2+a**2==b**2:
  print("triangle is right angled","\n")
else:
  print("triangle is not right angled","\n")


#Find the roots of a quadratic equation and display their nature
a, b, c = 1, 2, 5
d = (b**2) - 4 * a * c
print(f"{d} id the discriminant", "\n")
if d > 0:
  root1 = (-b + d**0.5) / (2 * a)
  root2 = (-b - d**0.5) / (2 * a)
  print(f"root1(real) is {root1} and root2(real) is {root2}", "\n")
elif d == 0:
  root = -b / (2 * a)
  print(f"root is {root}", "\n")
else:
  root1 = ((-d)**0.5) / (2 * a)
  root2 = -b / (2 * a)
  print(f"root1(img) is {root1} and root2(real) is {root2}", "\n")
