# Take a mark from user and check if number >100 or <0, which is invalid
# if the number is in between 0 and 100 display the valid mark

marks = input("Please enter the mark: ")
marks = int(marks)

# Check condition for >100 or <0

if(marks > 100 or marks<0):
    print("This is an invalid mark")
else:
    print("Valid mark")