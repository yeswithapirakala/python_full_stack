#continue
#The continue statement is used to skip the current iteration of a loop and jump to the next iteration, without stopping the loop completely (unlike break).

#without continue
for i in range(1, 7):
  print(i, end=" ")
print("\n")  #for next output in new line

#with continue
for i in range(1, 7):
  if i == 3:
    continue  #skips the iteration if i==3
  print(i, end=" ")
print("\n")

#if else with continue
for i in range(1, 10):
  if i % 2 == 0:
    continue
  print(i, end=" ")
print("\n")

#while statment with continue
i = 0
while i < 5:
  i += 1
  if i == 3:
    continue
  print(i, end=" ")
