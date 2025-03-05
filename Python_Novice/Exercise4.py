def to_str_fill(i):
  t = str(i).zfill(8)
  return t

# Create a list using list comprehension
s = [x**2 for x in range(10)]

# Modify the contents of the list using list comprehension
s = [x for x in s if x % 3 == 0]

# Call a function on the list elements using list comprehension
s2 = [to_str_fill(x) for x in s]

# Output the contents of the list using list comprehension
[print(x) for x in s2]