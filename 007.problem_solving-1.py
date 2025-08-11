#problem sloving ex-1

#convert km to miles
km=int(input("enter the the km :"))
miles=km*0.621371
print("the km in miles is : ",miles,"\n")

#convert celsius to fahrenheit
c=int(input("enter the the celsius :"))
f=(c*9/5) + 32
print("the celsius in fahrenheit is : ",f,"\n")

#convert fahrenheit to celsius
f=int(input("enter the the fahrenheit :"))
c=(f*5/9) - 32
print("the fahrenheit in celsius is : ",c,"\n")

#to slove qudratic equation
a,b,c=map(int,input().split())
numinator=((b**2)-(4*a*c))**0.5
denominator=2*a
root1=(-b + numinator) / denominator
root2=(-b -numinator) / denominator
print(root1,root2,"\n")

#calender
import calendar
print(calendar.month(2025, 7),"\n")

#swap two numbers without the temp
a=int(input("enter the first number :"))
b= int(input("enter the second number :"))
a,b=b,a
print(a,b,"\n")

#swap two numbers with assignment operator
a=int(input("enter the first number :"))
b= int(input("enter the second number :"))
a=a+b
b=a-b
a=a-b
print(a,b,"\n")

#check if the number is positive or negative
num=int(input("enter the number :"))
print("positive" * (num>0) + "negative" * (num<0) + "zero" * (num==0))

#to find number is odd or even
num=int(input("enter the number : "))
print("even" * (num%2==0) + "odd" * (num%2!=0))

#cheack to find leap year
year=int(input("enter the year: " ))
print("leap year" * (year%4==0) + "not leap year" * (year%4!=0))

#check the number is prime number or not
num=int(input("enter the prime number : "))
if num>1:
    for i in range(2,num):
      if num%i==0:
        print("not prime number")
        break
    else:
        print("prime")
else:
  print("not prime number")

#print all prime numbers in an interval 1-1000
for i in range(2, 1001):
  for j in range(2, i):
    if i % j == 0:
      break
  else:
    print(i)


#count vowels and consonents
s=input()
list='aeiouAEIOU'
v=0
c=1
for i in s:
  if i in list:
    v=v+1
  else:
    c=c+1
print(v,c)

#remmovie negatibve from 4,-3,5,-1,0
lst=[4,-3,5,-1,0]
res=[]
for ele in lst:
  if ele>=0:
    res.append(ele)
print(res)
 