#creating set
set = {1, 2, 3, 4, 5}
print(set, type(set), "\n")

#creating empty list
empty_set = set()
print(type(empty_set), "\n")

#creating user input set
u_set = input("enter the val: ")
my_set = set(u_set.split())
print(my_set, type(my_set), "\n")

u_set = set(map(int, input("enter the set:").split()))
print(u_set, type(u_set), "\n")

#updating sets
#add
a_set = {1, 2, 3}
a_set.add(4)
print(a_set, "\n")

#update
up_set = {1, 2}
ua_set = ([3, 4, 5])
up_set.update(ua_set)
print(up_set, "\n")

#add with 2 sets
a = {1, 2, 3}
b = {4, 5}
a.update(b)
print(a, "\n")

s = {"a"}
s.update("bc")
print(s, "\n")

#set operatins
#union
un1 = {1, 2, 3}
un2 = {4, 5, 6}
print(un1 | un2, "\n")

#intersection
i1 = {1, 2, 3}
i2 = {3, 4, 5}
print(i1 & i2, "\n")

#difference
d1 = {1, 2, 3}
d2 = {3, 4, 5}
print(d1 - d2, "\n")

#symentic difference
s1 = {1, 2, 3, 6}
s2 = {3, 4, 5}
print(s1 - s2, "\n")

#subset
sb1 = {1, 2}
sb2 = {1, 2, 3}
print(sb1.issubset(sb2), "\n")

#superset
sb1 = {1, 2}
sb2 = {1, 2, 3}
print(sb1.issuperset(sb2), "\n")

#dijoint
dj1 = {1, 2}
dj2 = {7, 8}
print(dj1.isdisjoint(dj2), "\n")

#setmethods
#add
ad = {1, 2, 3}
ad.add(4)
print(ad, "\n")

#update
up = {1, 2}
up.update([3, 4], {5})
print(up, "\n")

#remove
r = {1, 2, 3}
r.remove(2)
print(r, "\n")

#remove
dc = {1, 2, 3}
dc.discard(4)
print(dc, "\n")

#POP
p = {10, 20, 30}
x = p.pop()
print(x, "\n")

#clear
c = {1, 2, 3}
c.clear()
print(c)
