#anonoymous function 
#lamada arguments:expression

#add two numbers
add=lambda a:a+2
print(add(2),"\n")

#square of a number
square=lambda a:a*a
print(square(3),"\n")

#even
even=lambda a: True if a%2==0 else False
print(even(4),"\n")

#map()
l=[1,2,3,4,5]
l1=list(map(lambda a:a*a,l))
print(l1,"\n")

#filter()
l=[1,2,3,4,5]
l1=list(filter(lambda a:a%2==0,l))
print(l1,"\n")
print()