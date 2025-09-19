#File Operations
#Files can be handled with Python using the built-in open() function and methods like read(), write(), append(), and close().

#modes of file operations
#"r" → read (default, file must exist)
#"w" → write (creates/overwrites file)
#"a" → append (adds to end of file)
#"x" → create (error if file exists)
#"b" → binary mode (like "rb")
#"t" → text mode (default)

#Open
# open(file_name, mode)
f = open("example.txt", "w")  # open for writing
f.write("Hello, World!")

#Read
f = open("example.txt", "r")
print(f.read())       # Read entire file
# print(f.readline()) # Read one line
# print(f.readlines())# Read all lines as list
f.close()
print("\n")

#write
f = open("example.txt", "w")   # overwrite file
f.write("Hello, Python!\n")
f.write("Writing to file...")
f.close()

#append and close
f = open("example.txt", "a")   # append mode
f.write("\nThis line is appended.")
f.close()

#6. Directories
#Python has the os and os.path modules to handle directories.

#Remove Directory
import os

os.rmdir("my_folder")   # removes empty directory
print("Directory removed\n")


#Create Directory
import os

os.mkdir("my_folder")   # creates new directory
print("Directory created\n")

#Represent files in Directory
import os

files = os.listdir(".")   # list files in current directory
print("Files in current directory:", files,"\n")