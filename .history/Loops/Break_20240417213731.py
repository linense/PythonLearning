for i in range(1,11):
    if(i==5):
        break
    print(i)

number = input("Please enter your number: ")
for i in range(1,11):
    if(int(number)*i==60):
        break
    print(int(number)*i)

number = input("Please enter your number: ")
for i in range(1,11):
    print(int(number)*i)
    