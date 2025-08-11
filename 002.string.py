# lower()
text = "HELLO"
print(text.lower(),"\n")
#upper()
text = "hello"
print(text.upper(),"\n") 

#capitalize()
text = "python programming"
print(text.capitalize(),"\n")  

#title()
text = "hello world"
print(text.title(),"\n")  

# strip()
text = "   hello   "
print(text.strip(),"\n") 

#lstrip() 
text = "  hello  "
print(text.lstrip(),"\n")   

#rstrip()
text = "  hello  "
print(text.rstrip(),"\n")  

#replace(old, new)
text = "I like apples"
print(text.replace("apples", "oranges"),"\n")  

#find(sub)
text = "banana"
print(text.find("a"),"\n")  
print(text.find("z"),"\n")  

# index(sub)
text = "banana"
print(text.index("a"),"\n")  

# count(sub)
text = "banana"
print(text.count("a"),"\n")  

# startswith(sub)
text = "Hello"
print(text.startswith("He"),"\n")  

# endswith(sub)
text = "Hello"
print(text.endswith("lo"),"\n") 

# split(sep)
text = "I love Python"
print(text.split(),"\n")  

# join(list)
words = ['I', 'love', 'Python']
print(" ".join(words),"\n") 

# isalnum()
text = "abc123"
print(text.isalnum(),"\n")  

# isalpha()
text = "abc"
print(text.isalpha(),"\n") 

# isdigit()
text = "12345"
print(text.isdigit(),"\n")  

