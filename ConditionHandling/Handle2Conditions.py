# Take input from user - Number
# Check if number is even or odd
# Print either number with a corresponding message
data = input("Please enter your number: ")
data = int(data)

if(data%2==0):
    print(str(data) + " is an even number")
else:
    print(str(data) + " is an odd number")
