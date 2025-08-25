#pass
#The pass statement in Python does nothing.
#It is simply a placeholder used when a statement is required syntactically, but you don’t want any code to run.

#withou pass
for i in range(1, 5):
  print(i, end=" ")

print("\n")

#withspass
for i in range(1, 5):
  if i == 3:
    pass  #dosen't do anything
  print(i, end=" ")

print("\n")

#if else with pass
x = 10
if x == 10:
  pass
  print("pass statment\n")
else:
  print("x is not 10\n")

#while with else
i = 0
while True:
  i += 1
  if i == 5:
    pass  # does nothing
    break  # stop the infinite loop
  print(i, end=" ")
