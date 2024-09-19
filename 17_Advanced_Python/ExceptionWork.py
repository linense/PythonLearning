try:
    user_input1=input("Please enter first number: ")
    user_input2=input("Please enter second number: ")
    c=int(user_input1) + int(user_input2)
    print(c)
except:
    print("Your input is incorrect. Pls. enter correct data.")
finally:
    print("This comes always at the end of the code execution.")