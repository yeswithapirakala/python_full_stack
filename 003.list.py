#lists
#creating list
x = [1, 2, 3, 4, 5]
print(list, "\n")
#accessing list
y = [10, 0, -1, 7]
print(y[0], "\n")
print(y[1], "\n")
print(y[2], "\n")
print(y[3], "\n")
#taking user input for list
usrinp = [1, 2, 3, 4]
print(usrinp, "\n")

spl = "1 2 3 4"
splli = spl.split()
print(splli, "\n")

spl = "1 2 3 4"
splli = list(map(int, spl.split()))
print(splli, "\n")

#lst = list(map(int, input("Enter the list: ").split()))
#print(lst,"\n")

#list methods
#concat
l1 = [1, 2, 3]
l2 = [4, 5, 6]
print(l1 + l2, "\n")

#repeat
l1 = [1, 2, 3]
print(l1 * 3, "\n")

#append
my_list = [1, 2, 3]
print(my_list, "\n")
my_list.append(4)
print(my_list, "\n")

#extend
m_list = [1, 2, 3]
m_list.extend([3, "hi", 1.2])
print(m_list, "\n")

#insert
i_list = [1, 2, 3]
i_list.insert(1, "hi")
print(i_list, "\n")

#remove
r_list = [1, 2, 3, 4, 5, 1, 2, 1, 1]
r_list.remove(2)
print(r_list, "\n")

#pop
p_list = [1, 2, 3, 4, 5, 1, 2, 1, 1]
afpo = p_list.pop()
print(afpo, "\n")
print(p_list, "\n")

#pop with index
pi_list = [1, 2, 3, 4, 5, 1, 2, 1, 1]
afpoi = pi_list.pop(4)
print(afpoi, "\n")
print(pi_list, "\n")

#clear
c_list = [
    1,
    2,
    3,
    4,
    5,
]
print(c_list, "\n")
c_list.clear()
print(c_list, "\n")

#index
i_list = [1, 2, 3, 4, 5, 3, 5, 3, 2]
print(i_list, "\n")
print(i_list.index(3), "\n")

#count
c_list = [1, 2, 3, 4, 5, 3, 5, 3, 2]
print(c_list.count(3), "\n")

#sort
s_list = [1, 2, 3, 4, 5, 3, 5, 3, 2]
s_list.sort()
print(s_list, "\n")

#reverse sort
s_list = [1, 2, 3, 4, 5, 3, 5, 3, 2]
s_list.sort(reverse=True)
print(s_list, "\n")

#reverse
r_list = [1, 2, 3]
r_list.reverse()
print(r_list, "\n")

#copy
c_list = r_list.copy()
print(c_list, "\n")

#range
ra_list = list(range(1, 10))
print(ra_list, "\n")

