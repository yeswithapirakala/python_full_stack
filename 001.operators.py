a = 16
b = 4

# Arithmetic Operators
print("Arithmetic Operators \n")
print("a + b =", a + b)  # Addition
print("a - b =", a - b)  # Subtraction
print("a * b =", a * b)  # Multiplication
print("a / b =", a / b)  # Division (float)
print("a // b =", a // b)  # Floor Division
print("a % b =", a % b)  # Modulus
print("a ** b =", a**b, "\n")  # Exponentiation

# Relational (Comparison) Operators
print("Relational (Comparison) Operators \n")
print("a == b:", a == b)  # Equal to
print("a != b:", a != b)  # Not equal to
print("a > b:", a > b)  # Greater than
print("a < b:", a < b)  # Less than
print("a >= b:", a >= b)  # Greater than or equal to
print("a <= b:", a <= b, "\n")  # Less than or equal to

# Logical Operators
print("Logical Operators \n")
x = True
y = False
print("x and y:", x and y)  # Logical AND
print("x or y:", x or y)  # Logical OR
print("not x:", not x, "\n")  # Logical NOT

# Bitwise Operators
print("Bitwise Operators \n")
print("a & b =", a & b)  # Bitwise AND
print("a | b =", a | b)  # Bitwise OR
print("a ^ b =", a ^ b)  # Bitwise XOR
print("~a =", ~a)  # Bitwise NOT
print("a << 1 =", a << 1)  # Left shift
print("a >> 1 =", a >> 1, "\n")  # Right shift

# Assignment Operators
print("Assignment Operators \n")
c = a
print("c =", c)
c += b
print("c += b : ", c)
c -= b
print("c -= b :", c)
c *= b
print("c *= b:", c)
c /= b
print("c /= b :", c)
c //= b
print("c //= b :", c)
c %= b
print("c %= b :", c)
c = a
c **= b
print("c **= b :", c, "\n")

# Membership Operators
print("Membership Operators \n")
lst = [1, 2, 3, 10]
print("a in list:", a in lst)  # Membership test
print("b not in list:", b not in lst, "\n")

# Identity Operators
print("Identity Operators \n")
m = 10
n = 10
print("m is n:", m is n)  # Identity test
print("m is not n:", m is not n, "\n")
