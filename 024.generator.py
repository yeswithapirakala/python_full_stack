#generator
#A generator is a special type of function in Python that allows you to generate values one at a time, instead of returning them all at once like a normal function.
#you create a generator using the yield keyword.
def genetaor():
   yield 1
   yield 2
   yield 3
gen=genetaor()
for i in gen:
  print(i,end=" ")

print("\n")


#Difference between return and yield
#return → ends the function completely.
#yield → pauses the function, saves its state, and resumes when called again.

#generate squares
def squares(n):
  result=[]
  for i in range(1,n+1):
    result.append(i*i)
  return result
print(squares(6),"\n")

#febnocci series
def feb(n):
  a,b=0,1
  for i in range(n):
    yield a
    a,b=b,a+b
fib = feb(6)
for num in fib:
    print(num, end=" ")

print("\n")

#unsing next()
def even(n):
  for i in range(2,n+1,2):
    yield i
eve=even(10)
print(next(eve))
print(next(eve))
print(next(eve))
print(next(eve))
for i in eve:
  print(i,end="")