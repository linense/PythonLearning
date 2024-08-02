# Define tuples with ()
# Tuples cannot be changed
tuple1=(45, 'Testing', "www.thetestingworld.com",23.4,45)
print(tuple1[1])
print("Length of the tuple: " + str(len(tuple1)))
print("Number 45 occurs this many times in the tuples: " + str(tuple1.count(45)))
# Find index of any value in the tuple
print(tuple1.index(23.4))
# Merging tuples
tuple2=(1000,2000)
tuple3=tuple1+tuple2
print(tuple3)
# two ways of printing all values of a tuple
for i in tuple3:
    print(i)

i=len(tuple3)
for i in range(0,i):
    print(tuple3[i])