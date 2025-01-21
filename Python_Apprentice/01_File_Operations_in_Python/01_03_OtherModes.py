import os
file = open("example.txt", "r")
print(file.tell())
print(os.stat("example.txt").st_size) # returns the size of the file
print(file.read())
file.close()

f = open("example.txt", "r+") # File is now available for reading and writing, cursor is at the beginning
# There is also a+ mode: In a+, the cursor is at the end, in r+ at the beginning of the file
f.writelines("We are doing an r+ operation")
f.close()