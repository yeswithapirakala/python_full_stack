#1. Introduction to Regular Expression
#REGULAR EXPRESSIONS -> r
#purpose -> to find the pattern in the string,split the string,search the string,manipulate the string,test the string,string reputation,string validation

#METHODSI IN REGULAR EXPRESSIONS
import re #regular expression module

#search() -> return the match object if there is a match anywhere in the string
#syntax: re.search(pattern,string)

txt="the rain in spain"
x=re.search("the",txt)
print(x,"\n")

#match() -> return the match object if there is a match only at the beginning of the string
#syntax: re.match(pattern,string)
txt = "the rain in espana"
x = re.match("the", txt)
print(x,"\n")   # match (at start)

y = re.match("rain", txt)
print(x,"\n")   # None (not at start)


#findall() -> return a list containing all matches
#syntax: re.findall(pattern,string)
txt = "the rain in espana"
x = re.findall("in", txt)
print(x,"\n")   # ['in', 'in']

#split(pattern,string) -> return a list where the string has been split at each match
#syntax: re.split(pattern,string)
txt = "the rain in espana"
x = re.split("\s", txt)   # split at whitespace
print(x,"\n")   # ['the', 'rain', 'in', 'spain']

#sub() -> replace one or many matches with a string 
#syntax: re.sub(pattern,replacement,string)
txt = "the rain in espana"
x = re.sub("in", "OUT", txt)
print(x,"\n")   # the raOUT OUT spaOUT


#metacharacters-> . ^ $ * + ? {} [] \ | ()

#dot(.) -> matches any character except new line
print(re.findall("r.n", "ran ren r0n rnn"))  
# ['ran', 'ren', 'r0n', 'rnn']

#quesetion mark(?) -> matches zero or one occurrence of the preceding character
print(re.findall("colou?r", "color colour"))  
# ['color', 'colour']

#asterisk(*) -> matches zero or more occurrences of the preceding character
print(re.findall("go*gle", "ggle gooogle gogle"))  
# ['ggle', 'gooogle', 'gogle']

#plus(+) -> matches one or more occurrences of the preceding character
print(re.findall("go+gle", "ggle gooogle gogle"))  
# ['gooogle', 'gogle']

#caret(^) -> matches the start of the string
print(re.findall("^The", "The sun rises"))  
# ['The']

#dollar($) -> matches the end of the string
print(re.findall("end$", "This is the end"))  
# ['end']

#square brackets([]) -> used to specify a set of characters to match
print(re.findall("[aeiou]", "hello world"))  
# ['e', 'o', 'o']

#backslash(\) -> used to escape a special character
print(re.findall("\d", "12345"))
# ['1', '2', '3', '4', '5']

#curly braces({n}) -> used to specify the exact n number of occurrences 
print(re.findall("a{2}", "caaat aaa bbb"))  
# ['aa', 'aa']

#or(|) -> used to specify a set of characters to match
print(re.findall("cat|dog", "I love cats and dogs"))  
# ['cat', 'dog']

#1. Basic Project using Regular Expressions - Form Validaton
import re

email = "test@example.com"
phone = "9876543210"

# Email validation
if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
    print("Valid Email")
else:
    print("Invalid Email")

# Phone validation (10 digits only)
if re.match(r'^\d{10}$', phone):
    print("Valid Phone Number")
else:
    print("Invalid Phone Number")

