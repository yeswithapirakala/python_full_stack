"""1.Create a function that takes a list of strings and integers, and filters out the list so that it returns a list of 
integers only. 
Testcases: 
filter_list([1, 2, 3, "a", "b", 4]) ➞ [1, 2, 3, 4] 
filter_list(["A", 0, "Edabit", 1729, "Python", "1729"]) ➞ [0, 1729] 
filter_list(["Nothing", "here"]) ➞ []"""

def filter_list(input_list):
    return [i for i in input_list if isinstance(i, int)]
    #return list(filter(lambda x: isinstance(x, int), input_list))
input_list=[1, 2, 3, "a", "b", 4]
res=filter_list(input_list)
print(res,"\n")

#second  method
def f_lst(n):
  return [i for i in n if type(i) is int]

n=["A", 0, "Edabit", 1729, "Python", "1729"]
rest=f_lst(n)
print(rest,"\n")

#3rd method
def filter_list(s):
   lst=[]
   for i in s:
    if type(i) is int:
      lst.append(i)
   return lst

s=["Nothing", "here"]
re=filter_list(s)
print(re,"\n")

"""2.Given a list of numbers, create a function which returns the list but with each element's index in the list added 
to itself. This means you add 0 to the number at index 0, add 1 to the number at index 1, etc... 
Testcases: 
add_indexes([0, 0, 0, 0, 0]) ➞ [0, 1, 2, 3, 4] 
add_indexes([1, 2, 3, 4, 5]) ➞ [1, 3, 5, 7, 9] 
add_indexes([5, 4, 3, 2, 1]) ➞ [5, 5, 5, 5, 5]"""

def add_indexes(a):
  lst = []
  for i in range(len(a)):
    lst.append(a[i] + i)
  return lst

a = [0, 0, 0, 0, 0]
res = add_indexes(a)
print(res, "\n")

#secomd method
def add_i(b):
  return [i for i in range(len(b)) if b[i]+i]
a = [1, 2, 3, 4, 5]
res = add_indexes(a)
print(res, "\n")

#third method
#use enumerate function
def add_index(c):
  return [i+j for i,j in enumerate(c)]
  #return [i+j for i,j in enumerate(c) if i+j]
c = [5, 4, 3, 2, 1]
res=add_index(c)
print(res,"\n")

"""3..Create a function that takes the height and radius of a cone as arguments and returns the volume of the cone 
rounded to the nearest hundredth. See the resources tab for the formula. 
Testcases: 
cone_volume(3, 2) ➞ 12.57 
cone_volume(15, 6) ➞ 565.49 
cone_volume(18, 0) ➞ 0
"""
#first method
import math
def cone_volume(h,r):
  return round((1/3)*math.pi*r*r*h,2)
  #return round((1/3)*math.pi*r**2*h,2)
h=3
r=2
res=cone_volume(h,r)
print(res,"\n")

#second method
def cone_volume(h, r):
  return round((1/3) * 3.14 * r**2 * h, 2)

h = 15
r = 6
res = cone_volume(h, r)
print(res, "\n")

#third method
def cone_volume(h, r):
  height=h
  radius=r*r
  volume=(1/3)*3.14*radius*height
  return volume
h=18
r=0
res=cone_volume(h,r)
print(res,"\n")







