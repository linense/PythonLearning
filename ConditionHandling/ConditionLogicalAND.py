# Take 1 number from User
# Check if number is positive and multiple of 2, then print even number
# Check if number is positive and not multiple of 2, then print odd number

# Take input
num = input("Please enter your number: ")
num = int(num)

if((num >=0) and (num%2==0)):
    print("This is a positive even number")
elif((num>=0) and (num%2!=0)):
    print("This is a positive odd number")
else:
    print("This is a negative number")