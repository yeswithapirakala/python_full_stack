#while loop
#syntax: while condition:
#           statement

#basic example
#print 1 to 5
n=1
while n<=5:
  print(n,end=" ")
  n+=1
print("\n")


"""#1.example
str=""
while str!="exit":
  str=input("enter the string : ")
  print(str)"""

#sum of numbers from 1 to n
n=10
tot=0
i=1
while i<=n:
  tot+=i
  i+=1
print(tot,"\n")

#3. Reverse a number
num=1234
rev=0
while num>0:
  digit=num % 10
  rev=rev*10+digit
  num//=10
print(rev,"\n")

#4. Multiplication table of a number
n=7
i=1
while i<=10:
  print(f"{n} X {i} = {n*i}")
  i+=1
print("\n")

#5. Guess the number game
secret = 7
guess = None
while guess != secret:
    guess = int(input("Guess the number (1-10): "))
print("Correct!")



