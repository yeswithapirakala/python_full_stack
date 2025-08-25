#syntax def function_name(parameters:optimal):
#def ->keyword
#function_name -> name of the function
#parameters -> input to the function
#optimal -> optional

def add(a,b):     #function definition
    return a+b    # return value to the function definition
res=add(2,3)      #function call
print(res,"\n")    #output

##types of functions
#1.built in functions
#2.user defined functions

#user defined functions
#1.function without parameters and return type
def addition():
    a=10
    b=20
    print(a+b,"\n")
addition()

#2.function without parameters and with return type
def sub():
    a=20
    b=10
    return a-b
res=sub()           #user a variable to store the return value and print the variable
print(res,"\n")

#functions with parameters and without return type
def mul(a,b):
    print(a*b,"\n")
mul(10,20)

#functions with parameters and with return type
def div(a,b):
    return a/b
res=div(20,10)
print(res,"\n")

#built-in function

#int() -it converts the string input to integer
print(int(10.9),"\n")

#float() -it converts the string input to float
print(float(10),"\n")

#complex() - it converts the string input to complex
print(complex(10),"\n")

#str() - it converts the integer input to string    
print(str(11),type(str(11)),"\n")

#list() - it converts the string input to list    
#list is a collection of items
word ='Hexley'
print(list(word),"\n")

#tuple() - it converts the string input to tuple
word="Hexley"
print(tuple(word),"\n")

#set() - it converts the string input to set
word="Hexley"
print(set(word),"\n")

#dict() - it converts the string input to dictionary
word="Hexley"
print(dict(enumerate(word)),"\n")#The enumerate() function is a built-in Python function that lets you loop through an iterable (list, tuple, string, etc.) and automatically keep track of the index (position) of each item.


#chr() - it converts the integer input to character
print(chr(65),"\n")

#len() - it returns the length of the string
word="Hexley"
print(len(word),"\n")

#max() - it returns the maximum value in the string
#min() - it returns the minimum value in the string
#numbers
num=[1,2,3,4,5]
print(max(num),"\n")
print(min(num),"\n")

#strings
word="Hexley"
print(max(word),"\n") #lst character
print(min(word),"\n") #first character    

#sum - it returns the sum of the list
num=[1,2,3,4,5]
print(sum(num),"\n")

#all - it returns the boolean value
#True → if all elements in the iterable are True (non-zero, non-empty, not False).
num=[1,2,3,4,5]
print(all(num),"\n")

#False → if any element is False/0/empty
num=[1,2,3,4,5,0]
print(all(num),"\n")

#range - it returns the range of the list
#range(start,stop,step)
print(list(range(1,10,2)),"\n")

#reversed - it returns the reversed list
word="Hexley"
print(list(reversed(word)),"\n")

#sorted - it returns the sorted list
num=[1,3,4,2,6,0]
print(sorted(num),"\n")

#map()- it returns the map object   
#map(function,iterable)
#map() function applies a given function to each item of an iterable (list, tuple etc.) and returns a list of the results.
a = [1, 2, 3, 4, 5]
def m_sum(x):
    return x+1
print(list(map(m_sum, a)), "\n")

#enumerate() - it returns the index and the value pair
word="Hexley"
print(list(enumerate(word)),"\n")

#zip() - it returns the zip object
l1=[1,2,3,4,5]
l2=['a','b','c','d','e']
print(list(zip(l1,l2)),"\n")

#filter() - it returns the filter object
#filter(function,iterable)
def even(x):
    if x%2==0:
        return True
num=[1,2,3,4,5,]
l=list(filter(even,num))
print(l,"\n")

#abs()- it returns the absolute value
print(abs(-10),"\n")

#char() - it returns the character
print(chr(65),"\n")

#ord() - it returns the ASCII value
print(ord('A'),"\n")

#bin() - it returns the binary value
print(bin(10),"\n")

#hex() - it returns the hexadecimal value
print(hex(10),"\n")

#oct() - it returns the octal value
print(oct(10),"\n")

#pow() - it returns the power of the number
print(pow(2,3),"\n")

#round() - it returns the rounded value
print(round(10.5),"\n")







