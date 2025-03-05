# Create a function that accepts variable arguments as lists and named arguments
def fn(*args, kwargs):

    # Perform an operation on the list of arguments
    total = sum(args)
    retval = f'sum of args: {total}\n'

    # Perform an operation on the named arguments
    for k, v in kwargs.items():
        retval += f'{k}={v}\n'
        return retval

# Return different return values based on the arguments
s = fn(1,2,3, test=5, p='Hello, World!')
print(s)

t = fn(4,5,6, greeting='Hello', recipient='World')
print(t)  