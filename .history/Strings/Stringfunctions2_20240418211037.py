emailadress = "     testingworldindia@gmail.com       "
print(len(emailadress))

print(len(emailadress.lstrip()))
print(len(emailadress.rstrip()))
print(len(emailadress.strip()))

emailadress=emailadress.strip()
print(emailadress.replace("gmail", "yahoo"))

# Find how many l there are in the string
# Method 1: loop
z=0
for i in emailadress:
    if(i=="l"):
        z=z+1
print(z)
#Method 2:
x=len(emailadress)
y=len(emailadress.replace("l",""))
print(int(x-y))
