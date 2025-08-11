#conditional statments
#simple if
a = 10
b = 20
if a < b:
  print("a is greater than b", "\n")

#positive or negative
n = 10
if n > 0:
  print(f"{n} is a positive", "\n")
else:
  print(f"{n} is a negative", "\n")

#even or odd
n = 15
if n % 2 == 0:
  print(f"{n} is a even", "\n")
else:
  print(f"{n} is a odd", "\n")

#greater of two numbers
#greater of two numbers
a = 20
b = 10
if a < b:
  print("{} is greater than {}".format(b, a), "\n")
else:
  print("{} is greater than {}".format(a, b), "\n")

#largest among theree numbers
a, b, c = 10, 20, 30
if a > b and a > c:
  print(f"{a} is greater than {b} and {c}", "\n")
elif b > a and b > c:
  print(f"{b} is greater than {a} and {c}", "\n")
else:
  print(f"{c} is greater than {a} and {b}", "\n")

#check if num is divisible by 5 and 11
n = 55
if n % 5 == 0 and n % 11 == 0:
  print(f"{n} is divisible by 5 and 11", "\n")
else:
  print(f"{n} is not divisible by 5 and 11", "\n")

#leap year
year = 2025
if year % 4 == 0:
  print(f"{year} is a leap year", "\n")
else:
  print(f"{year} is not a leap year", "\n")

#a character is vowel or consonant
c = "a"
if c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
  print("{} is a vowel".format(c), "\n")
else:
  print(f"{c} the character is consonant")

#num is multiple of 3 or 7
n = 20
if n % 3 == 0 or n % 7 == 0:
  print(f"{n} is a multiple of 3 or 7", "\n")
else:
  print(f"{n} is not the multiple of 3 or 7", "\n")

#check the character is uppercase or lowercase,digit or special character
a = "$"
if a.isupper():
  print(f"{a} is upper", "\n")
elif a.islower():
  print(f"{a} is lower", "\n")
elif a.isdigit():
  print(f"{a} is digit", "\n")
else:
  print(f"{a} is special character", "\n")
