# Compare the strings
a="Testing"
b="testing"
if(a==b):
    print("Strings are equal")
else:
    print("Strings are not equal")
    
# Reverse the string
a="madam"
b=""
l=len(a)
for i in range((l-1),-1,-1):
    b=b+a[i]
print(a)
print(b)
if(a==b):
    print("This is a palendrome")
else:
    print("This is no palendrome")
    