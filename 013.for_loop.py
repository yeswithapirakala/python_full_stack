#for loop
#syntax : for variable in sequence

#1. Print numbers from 1 to 10
# Expected output: 1 2 3 4 5 6 7 8 9 10
for i in range(1,11):
  print(i,end=" ")
print("\n")    #newline


#2. Print the square of numbers from 1 to 5
# Expected output: 1 4 9 16 25
for i in range(1,6):
  print(i**2,end=" ")
print("\n")    #newline

#3. Print all even numbers from 1 to 20
# Expected output: 2 4 6 ... 20
for i in range(1,21):
  if i%2==0:
    print(i,end=" ")
print("\n")    #newline


"""#4. Sum of numbers from 1 to 100
# Expected output: 5050
n=(int(input(" ")))
sum=0
for i in range(n+1):
  sum=sum+i
print(sum,"\n")"""


#5. Print each character of the string "PYTHON" on a new line
# Expected output:
# P
# Y
# T
# H
# O
# N
s="PYTHON"
for i in range(len(s)):
  print(s[i],end="\n")
print("\n")  #newline

#6. Calculate factorial of a number n (e.g., n = 5)
# Expected output for n=5: 120
n=5
fact=1
for i in range(1,n+1):
  fact=fact*i
print(fact,"\n")

#7. Print the multiplication table of a number (e.g., 7)
# Expected output for 7:
# 7 x 1 = 7
# 7 x 2 = 14
# ...
# 7 x 10 = 70
n=7
for i in range(1,11):
  print(f"{n} X {i} = {n*i}","\n")


#8. Reverse a string using a for loop
# Example: "python" → "nohtyp"
s="python"
for i in s[::-1]:
  print(i,end="")
print("\n")
#9. Count vowels in a given string
# Example: "programming" → 3 vowels
s = "programming"
c=0
for i in s.lower():   
    if i in "aeiou":
        c =c+1
print(c,"\n")

#10. Print this pattern
"""
*
**
***
****
*****"""
for i in range(1,6):
  print("*"*i)

#count the vowels and conconants in "Python"
str = "Python"
c, v = 0, 0
for i in str.lower():
  if i in "aeiou":
    v += 1
  else:
    c += 1
print(f"vowels are {v} and consonants are {c}", "\n")

#remove negative numbers from the list
l = [4, -3, 5, -1, -2, 0]
l1 = []
for i in l:
  if i >= 0:
    l1.append(i)
print(l1, "\n")

