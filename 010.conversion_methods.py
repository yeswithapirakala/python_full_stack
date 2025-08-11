#conversion methods
#int to float and string
num = 24
print(float(num), "\n")
print(str(num), "\n")

#float to int and string
f = 24.0
print(int(f), "\n")
print(str(f), "\n")

#string to int,list,tuple,set
s1 = "123"
s2 = "abc123"
print(int(s1), "\n")
print(list(s2), "\n")
print(tuple(s2), "\n")
print(set(s2), "\n")

#list to string,set,tuple
lst = [1, 2, 'a', 'hexley']
print(str(list), "\n")
print(set(lst), "\n")
print(tuple(lst), "\n")

#list of tuples to dictonary
l = [('a', 1), ('b', 2), ('c', 3)]
print(dict(l), "\n")

#set to string,list,tuple
s = {1, 2, 3, 'a', 'hexley'}
print(list(s), "\n")
print(tuple(s), "\n")

#tuple to string,list,set
t = (1, 2, 3, 'hi')
print(list(t), "\n")
print(set(t), "\n")
print(str(t), "\n")
