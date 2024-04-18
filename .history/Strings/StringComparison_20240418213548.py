# Compare the strings
a="Testing"
b="testing"
if(a==b):
    print("Strings are equal")
else:
    print("Strings are not equal")
    
# Reverse the string
a="Testing"
b=""
l=len(a)
for i in range((l-1),-1,-1):
    b=b+a[i]
print(b)
    