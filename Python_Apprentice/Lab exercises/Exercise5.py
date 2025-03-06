# Create a List to be used as a stack
class Stack:
    def __init__(self, initial_values, max_size=None):
        if isinstance(initial_values, list):
            self.stack = initial_values
        else:
            self.stack = [initial_values]

        self.max_size = max_size
        self.size = len(self.stack)

    def push(self, value):
        if self.max_size:
            if self.size < self.max_size:
                self.stack.append(value)
                self.size += 1
            else:
                raise ValueError('Stack is full!')
        else:
            self.stack.append(value)
            self.size += 1
    def top(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def pop(self):
        if self.size > 0:
            if self.stack.pop():
                self.size -= 1
                return True
            return False

    def is_empty(self):
        if self.size == 0:
            return True
        return False

    def __len__(self):
        return self.size

    def __str__(self):
        return f'{self.stack}'
# Push elements onto the stack
stack = Stack(['Steve', 'Jane', 'Jim'])
stack.push('Alice')
stack.push('Bob')
print(stack.pop())

# Pop elements off of the stack
# Output the contents of the stack
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)

while len(stack) > 0:
  stack.pop()

if len(stack) == 0:
  print('Stack is empty!')


"""
Python Apprentice
2 Hr 34 Min Remaining
Exercise 5 - Use a List as a Stack
Introduction

Welcome to the Use a List as a Stack Python Lab. Your assignment for this exercise is to recognize how a Python list can be used as a stack by loading and unloading elements from the same end and to answer the assessment questions
Task

    Recognize how a Python list can be used as a stack by loading and unloading elements from the same end

    Create a List to be used as a stack
    Push elements onto the stack
    Pop elements off of the stack
    Output the contents of the stack

Instructions
Task 1 - Create a List to be used as a stack

    The first step in the exercise is to create a list to be used as a stack. Now you can do this directly, or you can incorporate the list inside of a stack class. We can implement some stack functions and carry out the exercise on the class itself. Define a class stack, and then I define the __init__ method to be used when the stack is instantiated. It has initial values as a parameter and max_size which defaults to none. But if we want, we can set a max_size of the stack, and prevent it from pushing new elements on to the stack if it is full, if it's reached the max_size. And then, inside the ¬¬__init__ method, check to see if isinstance of initial values is a list. So if it's a list, then we can set self.stack equal to those initial_values, otherwise, we set self.stack equal to initial_values wrapped in square brackets. We make the value itself if it's a single value, we make it into a list.

    We set self.max_size = max_size, which defaults to none. And self.size, the current size is equal to len(self.stack),

# Create a List to be used as a stack
class Stack:
  def __init__(self, initial_values, max_size=None):
    if isinstance(initial_values, list):
      self.stack = initial_values
    else:
      self.stack = [initial_values]

    self.max_size = max_size
    self.size = len(self.stack)

    Define the push function. push takes a value and it pushes it onto the list or appends it to the list. Then I check if self.max_size:, so if the variable is defined, check to see if self.size < self.max_size. If there's room on the stack, then append it to the stack variable to the list. Call stack.append value, and increment the size by 1, so + = 1, else raise a value error that says the stack is full. And then the else that corresponds to the max_size variable, if max_size is not defined, call self.stack.append(value_, and self.size + = 1 to increment it.

  def push(self, value):
    if self.max_size:
      if self.size < self.max_size:
        self.stack.append(value)
        self.size += 1
      else:
        raise ValueError('Stack is full!')
    else:
      self.stack.append(value)
      self.size += 1

    Define a top method, so many stacks have this top method that gets the top most element on the stack, but it doesn't actually pop it off. The pop checks to see if the stack is empty, so I call self.is_empty. And if that's true, it returns none, otherwise it returns self.stack index that- 1. That's the last element in the list, which we defined to be the top of the stack.

        Define the pop function, which checks to see if the size is greater than zero, and if it is, it calls self.stack.pop. Put the self.stack.pop in an if function because the pop function will return a value if there's one there. And then we can decrement the size by one and return true otherwise I return false.

        My is_empty method just checks to see if self.size is equal to zero and if it is it returns true. Otherwise it returns false, I implement the special function double underscore len. If the len function is called on our stack, it returns the size. And if a print function is called on our stack, or if it's turned into a string, it returns the string representation of the stack list. So it makes an f string of self.stack. 

 def top(self):
    if self.is_empty():
      return None
    return self.stack[-1]

 def pop(self):
    if self.size > 0:
      if self.stack.pop():
        self.size -= 1
        return True
    return False

 def is_empty(self):
    if self.size == 0:
      return True
    return False

 def __len__(self):
    return self.size

 def __str__(self):
    return f'{self.stack}'

Task 2 - Push elements onto the stack

    Now the next step of the exercise is to push some elements onto the stack. Create a stack equal to the stack class with the initial values, the list of strings, these names Steve, Jane and Jim. Then call stack.push on Alice. The string Alice, put another name and stack.push Bob, and then I print the contents of the stack

# Push elements onto the stack
stack = Stack(['Steve', 'Jane', 'Jim'])
stack.push('Alice')
stack.push('Bob')
print(stack)

Task 3 + 4

    Now we need to pop elements off of the stack and output the contents of the stack. Call print stack.pop, which will return true if there's an element to pop. I print the state of the stack at that point after that pop, I call pop again, so stack.pop, and then print the stack.

    One way we can iterate through all of the elements popping elements off of the stack is inside of a loop. We have while len(stack) > 0, so while there are elements on the stack call stack.pop. And after this executes the len of stack at this point should be zero and it should print stack is empty.

# Pop elements off of the stack
# Output the contents of the stack
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)

while len(stack) > 0:
  stack.pop()

if len(stack) == 0:
  print('Stack is empty!')

Terminal

    Now run the code, and then in the debug console, we get the output of the stack at various points in the program. So we start with Steve, Jane, Jim, Alice and Bob, so we initialize it with the first three names. Then we push Alice and Bob onto the stack, and then we call stack.pop. So that returns true, which leaves us with Steve, Jane, Jim and Alice and Bob is popped off at the top of the stack. We call pop again, which returns true and then Steve, Jane and Jim are left on the stack, and Alice is gone. Then we remove all of the elements in our loop, we pop all of them off the stack. And then at the end the stack is empty as expected, and that concludes the exercise.

terminal_app_05.png
Check your work

Check each box to confirm completion of the task.

    Create a List to be used as a stack
    Push elements onto the stack
    Pop elements off of the stack
    Output the contents of the stack

Question 1

Assume you push elements onto the stack in the following order.

stack = Stack(['Steve', 'Jane', 'Jim'])
stack.push('Alice')
stack.push('Bob')


What would be the first name "popped" off the stack?
Alice
Jane
Bob
Steve
Question 2

Assume you push elements onto the stack in the following order.

stack = Stack(['Steve', 'Jane', 'Jim'])
stack.push('Alice')
stack.push('Bob')


What would be the command print(stack.pop()) return?
['Steve', 'Jane', 'Jim', 'Alice', 'Bob']
['Bob', 'Alice', 'Jim', 'Jane', 'Steve']
True
False
Select Next below to move to the next exercise.
"""
