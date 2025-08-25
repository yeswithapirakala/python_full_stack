#pass by value
# in python immutable(int,float, string,tuple) are like pass by value(changes inside the function don’t affect the original).
#int()
def add(a):
  a = a + 1 ## this only changes local copy
  return a
a=10
res=add(a)
print(a,res,"\n")

#float()
def add(a):
  a = a + 1 ## this only changes local copy
  return a
a=10.5
res=add(a)
print(a,res,"\n")

#string()
def add(a):
  a = a + "jeon" ## this only changes local copy
  return a
a="hexley."
res=add(a)
print(a,res,"\n")

#tuple()
def add(a):
  a = a + (10,20) ## this only changes local copy
  return a
a=(1,2,3,4,5)
res=add(a)
print(a,res,"\n")

#pass by reference
# in python mutable(list,dict,set) are like pass by reference

#list()
def add(lst):
  lst.append(10)
  return lst ##this changes original
lst=[1,2,3,4,5]
res=add(lst)
print(lst,res,"\n") 

#dict()
def add(d):
  d["name"]="hexley"
  return d ##this changes original
d={"name":"jeon","age":20}
res=add(d)
print(d,res,"\n")

#set
def add(s):
  s.add(10)
  return s ##this changes original
s={1,2,3,4,5}
res=add(s)
print(s,res,"\n")

#recursion
#Recursion is when a function calls itself in order to solve a problem.

#factorial of a number
def fact(n):
  if n==1:
    return 1
  else:
    return n*fact(n-1)
print(fact(5),"\n")

#febonacci series
def feb(n):
  if n==0:
    return 0
  elif n==1:
    return 1
  else:
    return feb(n-1)+feb(n-2)
for i in range(10):
  print(feb(i),end=" ")
print("\n")


#sum of digits
def sums(n):
  if n == 0:     
      return 0
  else:
      return (n % 10) + sums(n // 10)

res = sums(1234)
print(res)
