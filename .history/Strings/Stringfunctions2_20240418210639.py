emailadress = "     testingworldindia@gmail.com       "
print(len(emailadress))

print(len(emailadress.lstrip()))
print(len(emailadress.rstrip()))
print(len(emailadress.strip()))

emailadress=emailadress.strip()
print(emailadress.replace("gmail", "yahoo"))

# Find how many l there are in the string
z=0
for i in emailadress:
    if i=="l":
        z=z+1
print(z)
