# Take input from user - Number
# Check if number negative; if yes, print this number
# Check if number is zero; if yes, print this number
# Check if number is positive; if yes, check if it is even or odd
# Print either number with a corresponding message
data = input("Please enter your number: ")
data = int(data)

if(data<0):
    print(str(data) + " is a negative number")
elif(data==0):
    print(str(data) + " is zero")
elif(data%2==0):
    print(str(data) + " is an even number")
else:
    print(str(data) + " is an odd number")