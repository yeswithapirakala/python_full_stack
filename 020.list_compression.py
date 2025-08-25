# list compression

l=[1,2,-3,4,-5,6,-7]
lst=[x for x in l if x>0]
print(lst,"\n")


#find the even numbers in the list[2,25,3,5,6,65,24,86,888] by sing compression
l=[2,25,3,5,6,65,24,86,888]
lst=[x for x in l if not x%2]
print(lst,"\n")

l=[2,25,3,5,6,65,24,86,888]
lst=[l[x] for x in range(len(l)) if not l[x]%2]
print(lst,"\n")

#if conditoon in single list in list compression
l=[2,25,3,5,6,65,24,86,888]
lst=[f"{x}->even" if x%2==0 else f"{x}->odd" for x in l]
print(lst,"\n")

#nexted  loop  in list comprehension
#outer loop followed by inner for loop
l=[(i,j)for i in range(1,6) for j in range(1,5)]
print(l,"\n")

#find total combination of two dice
l=[(i,j)for i in range(1,7) for j in range(1,7)]
print(l,"\n")

#find the combination of two dice with sum of 6
l=[(i,j)for i in range(1,7) for j in range(1,7) if i+j==6]
print(l,"\n")

#find the combination if any die contain 4
l=[(i,j)for i in range(1,7) for j in range(1,7) if i==4 or j==4]
print(l,"\n")

 #find the combination of two dice with target sum 8
target=8
l=[(i,j) for i in range(1,7) for j in range(1,7) if i+j==target]
print(l,"\n")

 #find the combination of two dice with target sum 8 but to  no repeat combination output [(2,6),(3,5),(4,4)]
l=[(i,j) for i in range(1,7) for j in range(1,7) if i+j==target and i<=j]
print(l,"\n")

#list comprehension l=[1,2,3,4,6,4,7] target=8\
l=[1,2,3,4,6,4,7]
lst=[(i,j) for i in l for j in l if i+j==8]
print(lst,"\n")

l = [1, 2, 3, 4, 6, 4, 7]
lst = [(l[i], l[j]) for i in range(len(l)) for j in range(i+1, len(l)) if l[i] + l[j] == 8]
print(lst,"\n")

