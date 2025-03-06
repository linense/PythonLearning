from collections import deque

# Implement a queue using the appropriate python collection
class Queue(object):
  def __init__(self, initial_values, max_size=None):
    self.queue = deque(initial_values)
    self.max_size = max_size
    self.size = len(initial_values)

  def push(self, value):
    if self.max_size:
      if self.size < self.max_size:
        self.queue.append(value)
        self.size += 1
      else:
        raise ValueError('Queue is full!')
    else:
      self.queue.append(value)
      self.size += 1

  def top(self):
    if self.is_empty():
      return None
    return self.queue[0]

  def pop(self):
    if self.size > 0:
      if self.queue.popleft():
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
    return f'{self.queue}'

queue = Queue(['Steve', 'Jane', 'Joe'], 6)
print(len(queue))
print()

# Add elements to the queue
queue.push('Alice')
queue.push('Bob')
queue.push('James')
#queue.push('Sally')
print(queue)
print(len(queue))
print()

# Pop elements from the queue in first-in, first-out fashion
print(queue.top())
queue.pop()
print(queue)
queue.push('Mallory')
print(queue)
print(queue.top())
print()

# Display the final contents of the queue
print(queue)

while len(queue) > 0:
  queue.pop()


"""
Introduction

Welcome to the Python Queues Python Lab. Your assignment for this exercise is to use the native Queue class of Python and perform standard queue operations on it and to answer the assessment questions
Task

    Use the native queue class of Python and perform standard queue operations on it

    Implement a queue using the appropriate Python collection
    Add elements to the queue
    Pop elements from the queue in first-in, first-out fashion
    Display the final contents of the queue

Instructions
Task 1 - Implement a queue using the appropriate Python collection

    For this exercise, from collections import deque, which is short for a double ended queue, which is contained in the collections library from the Python standard library.

    Now the first step of the exercise is to implement a queue using the appropriate Python collection. Well, the appropriate collection is a deque. Now, you could potentially do it with a list so you can implement a queue using a list, but it's inefficient to do so because of the way list is implemented. It's not recommended to use a list to implement a queue. If you're implementing a stack, a list is a perfectly fine data structure. But in this case with implementing a queue, we're going to use a deck. Now in our case, the queue is ‘a first in first out queue’, so a single ended queue, but we'll only be pulling off the front of the queue.

    We have a class queue, which extends the basic object. And then define the __init__ function, which takes the initial values and the max_size. We'll have an option to set a max size of our queue, and once it reaches that size, the queue will be full. Now this wasn't a strict requirement for this exercise, but include it so we can demonstrate how this could be done.

    We set self.queue = deque with the initial_values. Set self.max_size = max_size. And self.size is the number of elements in the initial_values or the len of initial_values. Define a push function, so we can push elements into the queue. And this takes a value that we're going to push. And then inside the body of the function, check to see if self.max_size: is set. If it's none, we just append the element to the queue, and increment the size by 1. So call self.queue.append parsing value as the argument, and set self.size += 1, to increment it by 1.

    If the max size is set, we make sure that the current size, self.size, is less than the max size. If it is, we call self.queue.append(value) and self.size +=1. Otherwise, raise a value error saying that the queue is full.

from collections import deque

# Implement a queue using the appropriate python collection
class Queue(object):
  def __init__(self, initial_values, max_size=None):
    self.queue = deque(initial_values)
    self.max_size = max_size
    self.size = len(initial_values)

  def push(self, value):
    if self.max_size:
      if self.size < self.max_size:
        self.queue.append(value)
        self.size += 1
      else:
        raise ValueError('Queue is full!')
    else:
      self.queue.append(value)
      self.size += 1

    The next method is a method called top. This is the first element or the current element in the queue that's next to come off. Checked to see if the queue is empty, so if self.is_empty() is true then return none, so there's no element in the queue. Otherwise, return self.queue at index 0, so this is the first element in the queue. Define def pop, so it's a pop function that will pop the current element off of the queue. Check to see if the size is greater than 0. If it is, then there are items that we can pop from the queue. And then call self.queue.popleft. Popping left pops the first element off, and popping if we just call pop on queue, it will pop the rightmost element off. But that would be pulling from the queue from the wrong end because we want it in ‘first in first out’ fashion. So if this is true, if there's an element to pop off, then decrement the size. So self.size -=1, and return true saying that the pop was successful, otherwise return false. If we call pop on an empty queue, it will return false.

    We have def is_empty, so this is an empty function, checks the self.size and if it's 0 it returns true, otherwise it returns false. Define a __len__ special function to return the size. If the len function is called on the queue, so I returned self.size, and the __str__ or string representation of the queue, which returns the f string of self.queue, which will output the values that are currently in the queue.

    Now we can continue with the exercise, start by initializing the queue, so we have queue = Queue class. So we're creating an instance with the list of initial values being Steve, Jane and Joe, and the max_size to be 6. We can have 6 elements in this queue before we reach the limit. Then call print len of queue to see how many elements are currently in the queue. At this point, it should be 3. Print an empty line.

  def top(self):
    if self.is_empty():
      return None
    return self.queue[0]

  def pop(self):
    if self.size > 0:
      if self.queue.popleft():
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
    return f'{self.queue}'

queue = Queue(['Steve', 'Jane', 'Joe'], 6)
print(len(queue))
print()

Task 2 - Add elements to the queue

    The next step of the exercise, is to add elements to the queue. So we call queue.push on the following strings, the following names, Alice, Bob, James and Sally. So if we count how many names we have to this point, we have three initially, and then we add four more. Sally will be the seventh name, so we should see a problem here with the max size if it's done correctly.

    And then after that, print the queue, print the len of queue, and then print an empty line.

# Add elements to the queue
queue.push('Alice')
queue.push('Bob')
queue.push('James')
#queue.push('Sally')
print(queue)
print(len(queue))
print()

Task 3 - Pop elements from the queue in first-in, first-out fashion

    Now we are going to pop the elements. So we're popping elements from the queue in ‘first in, first out’ fashion. The first one in is Steve, so that's the one that should be popped out. Print queue.top to make sure it is Steve then call queue.pop, and print the queue. Push another name, queue.push Mallory. Print this state of the queue at that point, and then print queue.top, and an empty print.

# Pop elements from the queue in first-in, first-out fashion
print(queue.top())
queue.pop()
print(queue)
queue.push('Mallory')
print(queue)
print(queue.top())
print()

Task 4 - Display the final contents of the queue

    Then we display the final contents of the queue by printing queue. And then, while len of queue is greater than 0, I call queue.pop to remove everything off of the queue.

# Display the final contents of the queue
print(queue)

while len(queue) > 0:
  queue.pop()

Terminal

    Now We run the program and see what happens in the debug console. At the very bottom, we see value error queue is full, and that's what we expected when we pushed Sally onto the queue. If we scroll up, we get the three printed from line 45 or we printed the len of queue, but then it only gets to line 52 before it fails. So we’re going to comment out queue.push of Sally on line 52, so that we can see the rest of the program execute successfully.

    Now run the program again, and in this case, we get more output. We get the queue printed which is a deque from line 53 with Steve, Jane, Joe, Alice, Bob and James. And then call the length which is 6. And then top at this point is Steve, call pop, and then print the queue again. In this case, it starts at Jane, and then Joe, Alice, Bob and James with Steve being popped off the front of the queue. And then push Mallory onto the queue. And then at this point, the top of the queue is Jane, so when we print the results, we have Jane, Joe, Alice, Bob James, and Mallory. And that concludes this exercise.

terminal_app_06.png
Check your work

Check each box to confirm completion of the task.

    Implement a queue using the appropriate Python collection
    Add elements to the queue
    Pop elements from the queue in first-in, first-out fashion
    Display the final contents of the queue

Question 1

Which of the following are valid methods used to add an item to a Python queue?
append
push
put
insert
Question 2

Which of the following are valid methods used to retrieve an item to a Python queue?
put
get
push
insert

Select Next below to move to the next exercise.
"""