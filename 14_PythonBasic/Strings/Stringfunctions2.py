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
#Method 2: use len-Function
x=len(emailadress)
y=len(emailadress.replace("l",""))
print(int(x-y))

# find a substring
a="gmail"
print(emailadress.find(a))

# use of split function
emailadress="this is my email adress testingworldindia@gmail.com"
list1=emailadress.split(" ")
print(list1)
