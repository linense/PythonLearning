import numpy as np

def print_var(n, x):
  print(f'{n}: {x} {type(x)}')

x = 2**99
print_var('x', x)

# Create a variable to hold a 64-bit integer
y = np.int64(2**33)
print_var('y', y)

# Create a variable to hold a double floating point number
z = np.float64(387438.238439843934329)
print_var('z', z)

# Convert the 64-bit integer to a 32-bit integer
y2 = y.astype(np.int32)
print_var('y2', y2)

y3 = np.int32(np.int64(2**31))
print_var('y3', y3)

# Convert the double floating point number to a single floating point number
z2 = np.float32(z)
print_var('z2', z2)

