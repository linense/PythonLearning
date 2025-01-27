import os

#var = "xyz"

try:
   # f = open('nonexistent_file')
   print(var)
except FileNotFoundError:
    print("File Not Found!")

except OSError:
    print("OS Error")

except:
    print("Other error.")

finally:
    print("The try except block has ended.")