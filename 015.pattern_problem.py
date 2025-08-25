"""* * * *
* * * *
* * * *
* * * *"""
n=4
for i in range(n):
  for j in range(n):
    print("*",end=" ")
  print()

print()

"""
1 1 1 1
2 2 2 2
3 3 3 3
4 4 4 4
"""
n=[1,2,3,4]
for i in range(len(n)):
  for j in range(len(n)):
    print(n[i],end=" ")
  print()
print()

"""
1 2 3 4
1 2 3 4
1 2 3 4
1 2 3 4
"""
n=[1,2,3,4]
for i in range(len(n)):
  for j in range(len(n)):
    print(n[j],end=" ")
  print()
print()

"""
*
* *
* * * 
* * * *  
"""
n=4
for i in range(n):
  for j in range(n):
    if j<=i:
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print()

print()

"""
* * * *
* * * 
* *
*
"""
for i in range(n):
  for j in range(n):
    if j>=i:
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print()
print()

"""
# # # #
#     #
#     #
# # # #
"""
n=4
for i in range(n):
  for j in range(n):
    if i==0 or i==n-1 or j==0 or j==n-1:
      print("#",end=" ")
    else:
      print(" ",end=" ")
  print()
print()

