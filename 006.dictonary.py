# Basic
my_dict = {"name": "hexley", "age": 22, "city": "Hyderabad"}
print(my_dict,type(my_dict),"\n")

# Using dict()
my_dict2 = dict(name="hexley", age=30)
print(my_dict2,type(my_dict2),"\n")

#empty dict
empty_dict = {}
print(empty_dict,"\n")

'''#user input
l=int(input("enter the dict length: "))
d={}
for i in range(l):
    key=input("enter the key:")
    value=input("enter the value:")
    d[key]=value
print("dictonary",d,"\n")'''

#adding and updating
dict_u={"name":"hexley","city":"Hyderabad"}
dict_u["age"]=22
dict_u.update({'name': 'yeswitha'})
print(dict_u,"\n")

#accessing
dict_a={"name":"hexley","city":"Hyderabad"}
print(dict_a["name"],"\n")

#removing
dict_r={"name":"hexley","city":"Hyderabad",
       "age":22,}
print(dict_r,"\n")
del dict_r["age"]
print(dict_r,"\n")

#dictonary methods
#keys()
k={"name":"hexley","city":"Hyderabad",
       "age":22,}
print(k.keys(),"\n")

#values()
v={"name":"hexley","city":"Hyderabad",
         "age":22,}
print(v.values(),"\n")

#items()
i={"name":"hexley","city":"Hyderabad",
       "age":22,}
print(i.items(),"\n")

#pop()
p={"name":"hexley","city":"Hyderabad",
       "age":22,}
print(p.pop("age"),"\n")

#popitem()
pi={"name":"hexley","city":"Hyderabad",
       "age":22,}
print(pi.popitem(),"\n")

#get()
g={"name":"hexley","city":"Hyderabad",
       "age":22,}
print(g.get('name'),\"n") 

#copy and clear
c1={"name":"hexley","city":"Hyderabad",
       "age":22,}
c2=c1.copy()
print(c1,c2,"\n")
c1.clear()
print("c1",c1,"\n")








