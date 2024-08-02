# Take 1 numeric input from user, check if number is positive or negativ
# If negative, display the number
# If positive, check if it is even or odd

# Take input from user and convert to int
data = input("Please enter your number: ")
data = int(data)

if(data<0):
    print(str(data) + " is a negative number")
else:
    if(data%2==0):
        print(str(data) + " is an even number")
    else:
        print(str(data) + " is an odd number")