#break
#decreases the number of iterations
for i in range(1, 10):
  if i == 5:
    break
  print(i, end=" ")
print("\n")

#without break
n = 10
iter_val = 0
for i in range(n):
  if i == 5:
    print(i, end=' ')
  else:
    print(i, end=' ')
  iter_val += 1
print()
print("iterable val:", iter_val, "\n")

#with break
n = 10
iter_val = 0
for i in range(n):
  if i == 5:
    print(i, end=' ')  #end='' prints the output in same line
    break
  else:
    print(i, end=' ')
  iter_val += 1
print()  #gives print in another line
print("iterable val:", iter_val, "\n")

#for loop with else
l = [1, 2, 3, 4, 5]
for num in l:
  if 4 == num:
    print("4 in list \n")
    #break
else:
  print("not in list \n")

#while loop with else
n = 1
while True:
  if n == 5:
    print("5 in list \n")
    break
  n += 1
