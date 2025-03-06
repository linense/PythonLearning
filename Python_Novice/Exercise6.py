# Create a global variable
g_x = 2.5

# Create a function that uses the global variable and a local one
def f1(x):
  global g_x
  y = 6
  g_x = x * y
  return g_x

# Attempt to reference a function's local variable outside of the function
#print(y)

# Print the function's return value
print(f'f1(5): {f1(5)}')
print(f'g_x: {g_x}')

print(f'f1(g_x): {f1(g_x)}')
print(f'g_x: {g_x}')