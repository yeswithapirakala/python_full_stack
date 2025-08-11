#creating tuple
t = (1, 2, 'a', 'codegnan', 5.5, 2, 1, [1, 23, 45], 10)
#intilizing tuple
t1 = ()  #empty tuple
t2 = (1, 2, 3)  #tuple with multiple values
t3 = (1, )  #tuple with single value
print(type(t1), type(t2), type(t3), "\n")

#indexing and slicing
is_tuple = (1, 2, 'a', 'codegnan', 5.5, 2, 1, [1, 23, 45], 10)
print(is_tuple[4], "\n")
print(is_tuple[-4], "\n")
print(is_tuple[-4:-1], "\n")
print(is_tuple[-3:2:1], "\n")  #infinite loop
print(is_tuple[-3:2:-1], "\n")  #finiteloop
print(is_tuple[5:100:1], "\n")

#user input of tuple
#u_tuple=tuple(map(int,input("Enter the tuple: ").split()))
#print(u_tuple,"\n")

#concatenation
t1 = (1, 2, 3)
t2 = (1, 3, "hi")
print(t1 + t2, "\n")

#repat
r_tuple = (1, 2, 3)
print(r_tuple * 2, "\n")

#count
c_list = (1, 2, 3, "hi", 1, [1, 2, 3], 10)
print(c_list.count(1), "\n")
print(c_list.count([1, 2, 3]), "\n")

#index
i_list = (1, 2, 3, "hi", 1, [1, 2, 3], 10)
print(c_list.index(1), "\n")
print(c_list.index([1, 2, 3]), "\n")

#bultin functions
b_tuple = (1, 2, 3, 4, 5)
print(len(b_tuple), "\n")
print(min(b_tuple), "\n")
print(max(b_tuple), "\n")
print(sum(b_tuple), "\n")

#sorted
s_tuple = (1, 5, 3, 7, 2, 9, 4)
s_tupleop = sorted(s_tuple)
print(s_tupleop, "\n")

#convert list to tuple
list = [1, 2, 3, 4, 5]
cov_list = tuple(list)
print(cov_list, "\n")
print(type(list), type(cov_list), "\n")

#membership
m_tuple = [1, 2, 3, 4, 5]
print(2 in m_tuple, "\n")
print(7 in m_tuple, "\n")

n_tuple = [1, 2, 3, 4, 5]
a, *b, c = n_tuple
print(a, b, c, "\n")
