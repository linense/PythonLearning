list1=[34,34.22,"Testing", 55, 89, "World"]

# Fetch item by index
print(list1[1])

# Fetch range of index
print(list1[1:4])

# Starting index only
print(list1[2:])

# End index only      
print(list1[:4])

# Update list
list1[3]=100
print(list1)

# Insert value, rest will be shifted
list1.insert(3,"ABCD")
print(list1[3])
print(list1)

# Remove value only on first occurrence
list1.remove(100)
print(list1)

# Show length of the list
print(len(list1))
list1.insert(4,"another item")
print(len(list1))

# Concatenate lists
list2=[1,2,3]
list3=list1+list2
print(list3)