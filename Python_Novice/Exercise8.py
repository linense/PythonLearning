# Create a python function
def fn_next(begin):
  current = begin

  # Create an inner function to act as a closure
  def fn_inc():
    nonlocal current
    current += 1
    return current
  return fn_inc

# Return the closure function object
get_next = fn_next(100)

# Call the function to return a value that changes each time it is called
print(get_next())
print(get_next())
print(get_next())
print(get_next())
print(get_next())
print(get_next())
print(get_next())