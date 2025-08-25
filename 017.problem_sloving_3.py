#function problems


#write a function,return the n even numbers
def even_numbers(n):
  l = []
  for i in range(n):
    l.append(2 * i)
  return l


res = even_numbers(10)
print(res, "\n")


#write a function,return the n odd numbers
def odd_numbers(n):
  l = []
  for i in range(n):
    l.append(2 * i + 1)
  return l


res = odd_numbers(10)
print(res, "\n")

#convert list to string
l = [65, 68, 72, 99, 102]
a = "".join(map(chr, l))
print(a, "\n")

#write a program to find sum of elements in list
l = [1, 2, 3, 4, 5]
sum = 0
for i in l:
  sum = sum + i
print(sum, "\n")

#write a python program to multiply all the numbers in a list
l = [1, 2, 3, 4, 5]
mult = 1
for i in l:
  mult = mult * i
print(mult, "\n")


#write a python program to find largest number in a list
def find_max(l):
  return max(l)


l = [1, 2, 3, 4, 5]
print(find_max(l), "\n")


#write a python program to find smallest number in a list
def find_min(l):
  return min(l)


l = [1, 2, 3, 4, 5]
print(find_min(l), "\n")


#write a python program to find second largest number in a list
def second_max(l):
  l.sort()
  return l[-2]


l = [1, 2, 3, 4, 5]
print(second_max(l), "\n")
"""#write a program to find n th largest number in a list
def nth_lm(l):
  l.sort()
  return l[-lrnumber]
l=list(map(int,input().split()))
lrnumber=int(input("enter the nth number"))
print(nth_lm(l),"\n")"""


#write a python program to print even numbers in a list
def even(l):
  if l % 2 == 0:
    return l


num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l = list(filter(even, num))
print(l, "\n")


#write a python program to print odd numbers in a list
def odd(l):
  if l % 2 != 0:
    return l


num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l = list(filter(odd, num))
print(l, "\n")


# add index to the element in the list
def add_indexes(lst):
  res=[]
  for i in range(len(lst)):
    res.append(lst[i]+i)
  return res
print(add_indexes([0,0,0,0,0]))

#find the missing number in the list between the 1 to 10
def missing_num(lst):
  for i in range(1,11):
    if i not in lst:
      return i
print(missing_num([1,2,3,4,6,7,8,9,10]))

#take input list and add the number at the end and remove the first elements from the list
def next_in_line(lst,num):
  if len(lst)==0:
    return "no list has been selected"
  else:
    lst.append(num)
    lst.remove(lst[0])
  return lst
print(next_in_line([5,6,7,8,9],1),"\n")

#function that takes list of dictionaries and ads the sum of people's budget
def list_dict(lst):
  sum=0
  for i in lst:
    sum=sum+i["budget"]
    return sum

print(list_dict([{"name": "Alice", "age": 30, "budget": 23000},
        {"name": "Bob", "age": 25, "budget": 40000},
        {"name": "Charlie", "age": 35, "budget": 2700}
                ]),"\n")

#list of 1 to 10
l=[]
for i in range(1,11):
  l.append(i)
print(l,"\n")

lt=[i for i in range(1,11)]
print(lt,"\n")

#print list even numbers between 1 to 20
even=[x for x in range(1,21) if x%2==0]
print(even,"\n")

#print list even numbers between 1 to 20 without using '==',and '!=' operator'
odd=[x for x in range(1,21) if x%2 ]
print(odd,"\n")


#  Example
if False:
  print("hello")
else:
  print("hi","\n")

#given a string of numbers seperated by a comma and space,return product of all numbers
def multiply_num(n_list):
  product = 1
  for num in n_list:
      product *= num
  return product

s = input()  
n_list = list(map(int, s.split()))
print(multiply_num(n_list))

#squares of every digit of numbers
def square_digits(n):
  res=[]
  for i in n:
    res.append(int(i)**2)
  return res
n = int(input())
print(square_digits(n))

