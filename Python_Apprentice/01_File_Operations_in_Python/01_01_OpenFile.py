
file = open("sample.txt")
print(file.mode) # prints "R", as file is opende in Read mode
print(file.name) # prints "sample.txt", the name of the file
print(file.read()) # prints the entire content of the file
print(file.closed) # prints the status of the file, here "False" as the file is open
file.seek(0) # positions the cursor at the beginning
print(file.read(5)) # reads the first 5 characters
print(file.tell()) # shows the position of the cursot (5)
print(file.read(5)) # reads the next 5 characters
file.close()