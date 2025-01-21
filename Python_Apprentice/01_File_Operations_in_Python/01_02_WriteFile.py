file = open("example.txt", "w") # overwrites the file, if it exists
file.write("Let's check the write operation")
file.seek(6) # positions the cursor and overwrites the text at this position
file.write(" examine ")
file.close()

file = open("sample.txt")
for lines in file:
    print(lines)
file.close()

with open("example.txt", "w") as f:
    f.write("First line\n")
    f.write("Second line\n")
    f.write("Third line\n")

f = open("example.txt", "a")
print(f.tell())
f.writelines(["Another line was appended\n", "What will it look like now\n", "Let's check it out\n"])

f.close()
f = open("example.txt", "r")
print(f.readlines())
print(f.fileno())
print(f.readable())
print(f.writable())
f.close()