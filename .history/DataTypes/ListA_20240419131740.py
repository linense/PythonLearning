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

# Insert value, rest will be shifted
list1.insert(3,"ABCD")
print(list1[3])
print(list1)

# Remove value only on first occurrence
list1.remove(55)
print(list1)