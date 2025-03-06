# Create a class to implement a binary search tree
class Node:
  def __init__(self, value):
    self.value = value
    self.right = None
    self.left = None

# Implement an insertion method
  def insert(self, value):
    if self.value != value:
      if value > self.value:
        if self.right is None:
          self.right = Node(value)
        else:
          self.right.insert(value)
      elif value < self.value:
        if self.left is None:
          self.left = Node(value)
        else:
          self.left.insert(value)

# Implement a method to traverse the tree in depth-first order
  def depth_traversal(self, node):
    items = []
    if node:
      items.append(node.value)
      items = items + self.depth_traversal(node.left)
      items = items + self.depth_traversal(node.right)
    return items

# Implement a method to traverse the tree in breadth-first order
  def breadth_first(self, node):
    items = []
    if node:
      items = self.breadth_first(node.left)
      items.append(node.value)
      items = items + self.breadth_first(node.right)
    return items
  
# Create an instance of the tree and insert data
node = Node(10)
node.insert(5)
node.insert(25)
node.insert(12)
node.insert(33)
node.insert(18)

# Display the data points in their traversal orders
print('Depth first order: {}'.format(node.depth_traversal(node)))
print('Breadth first order: {}'.format(node.breadth_first(node)))

"""
Introduction

Welcome to the Tree Traversal Python Lab. Your assignment for this exercise is to traverse a Binary Search Tree (BST) in depth-first and breadth-first order in Python and to answer the assessment questions
Task

    Traverse a Binary Search Tree (BST) in depth-first and breadth-first order in Python

    Create a class to implement a binary search tree
    Implement an insertion method
    Implement a method to traverse the tree in depth-first order
    Implement a method to traverse the tree in breadth-first order
    Create an instance of the tree and insert data
    Display the data points in their traversal orders

Instructions
Task 1 - Create a class to implement a binary search tree

    The first step is to create a class to implement a binary search tree. For this, we start with a class Node. And in this class, we define a __init__ method that takes a value, the value for that particular node.

    We have self.value = value. Since it's a binary search tree, we have two branches, which we typically call right and left. The right branch or a right node points to another node that has a value greater than the current one. And the left branch or left node will eventually point to another node that has a value less than the current value. The right takes greater values and the left takes lesser values.

# Create a class to implement a binary search tree
class Node:
  def __init__(self, value):
    self.value = value
    self.right = None
    self.left = None

Task 2 - Implement an insertion method

    Then the next step is to implement an insertion method. We have def insert, and this takes a value. What happens here is a bit of logic that's very important so that we can handle all of the cases of where to insert a node. The first thing we check if self.value, so if the current node is not equal to the value. Then we check to see if the value is greater than the current value, so greater than self.value. And if self.write is none, if it is a greater value, we look to the right branch. And if it's none, then we set self.write = node of the value.

    We insert the node when we reach none. Otherwise, we call self.write.insert. We can think of it as recursively going down the rightmost nodes until we reach this place where we can insert the value. elif value is less than self.value. If the value is less than the current value of the current node, then if self.left is None, then we set self.left = Node(value). We create a new node, which left points to, otherwise we take self.left and we call its insert method with the value. Now what if the value is the same? Now in this solution, we’re assuming that the values are unique. If the value is equal, we assume that it's already there and we don't need to insert it again. So there are no duplicate values.

# Implement an insertion method
  def insert(self, value):
    if self.value != value:
      if value > self.value:
        if self.right is None:
          self.right = Node(value)
        else:
          self.right.insert(value)
      elif value < self.value:
        if self.left is None:
          self.left = Node(value)
        else:
          self.left.insert(value)

Task 3 - Implement a method to traverse the tree in depth-first order

    Then we need to implement a method to traverse the tree in depth first order. We want to go down the nodes of the tree till we reach the bottom, and then we insert the node value. Set this items variable equal to an empty list. We'll add the values to this list in the order that we traverse them. Now if node is set, so if it's none, we take items.append the node value. Then we take items = items + the result of self.depth traversal of the left nodes. And items = items + self.depth traversal of the right node.

    We're going down the nodes, down the left nodes and down the right nodes. Now since this is being called recursively, we're calling depth traversal with each node starting with the left and going down the left most branches and then the right most branches. And this will recursively build up the items with all of the nodes that are traversed. And then in the end we return items, so it doesn't return items until it's traversed down the depth of an entire branch.

# Implement a method to traverse the tree in depth-first order
  def depth_traversal(self, node):
    items = []
    if node:
      items.append(node.value)
      items = items + self.depth_traversal(node.left)
      items = items + self.depth_traversal(node.right)
    return items

Task 4 - Implement a method to traverse the tree in breadth-first order

    The next step is to implement a method to traverse the tree in breadth_first order. There are a number of ways we can do this depending on how we view this breadth_first. We want to think of going from left to right. We start at the left branch, and we move across the graph to the rightmost. So breadth_first takes a node. It sets items equal to an empty list, so the items to be returned. And then if we have a valid node, we set items = self.breadth_first(node.left). It goes to the leftmost, and we'll work our way across to the rightmost.

    We take our left, then items.append(node.value), and then items = items + self.breadth_first(node.right). We go from leftmost and then we queue up all of the rightmost. We're going across the graph. And we’re doing it this way so that we move across the graph, and this will pick up the nodes in sorted order. Now there are a couple of different ways we can do breadth_first order. We can do it level by level going from left to right. Or we can also do it in a traversal that's picking up all of the nodes from the leftmost, which would be at the lowest level to the rightmost. And that's what I'm doing here. And then in the end, it returns items.

# Implement a method to traverse the tree in breadth-first order
  def breadth_first(self, node):
    items = []
    if node:
      items = self.breadth_first(node.left)
      items.append(node.value)
      items = items + self.breadth_first(node.right)
    return items

Task 5 - Create an instance of the tree and insert data

    The next step is to create an instance of the tree and insert the data. Create a node = Node with value 10. We have a single node, we think of this as the root node, the first node we add. Then I called node.insert with the value 5, node.insert with 25, 12, 33, and 18. Insert these six values.

# Create an instance of the tree and insert data
node = Node(10)
node.insert(5)
node.insert(25)
node.insert(12)
node.insert(33)
node.insert(18)

Task 6 - Display the data points in their traversal orders

    Then the final step is to display the data points in their traversal orders. print(depth first order: followed by the result of the node.depth_traversal starting at the root node. And then breadth first order where we call node.breadth_first and we insert that into the string.

# Display the data points in their traversal orders
print('Depth first order: {}'.format(node.depth_traversal(node)))
print('Breadth first order: {}'.format(node.breadth_first(node)))

Terminal

    Now if I run the program, We get the results printed in the debug console. So depth first order gives us 10, 5, 25, 12, 18, and 33. And breadth first order going from leftmost to rightmost, we get 5, 10, 12, 18, 25, and 33, giving us the results in sorted order. And that concludes this exercise.

terminal_app_08.png
Check your work

Check each box to confirm completion of the task.

    Create a class to implement a binary search tree
    Implement an insertion method
    Implement a method to traverse the tree in depth-first order
    Implement a method to traverse the tree in breadth-first order
    Create an instance of the tree and insert data
    Display the data points in their traversal orders

Question 1

Which of the following would complete the code to traverse a Binary Search Tree in depth-first order?

def depth_traversal(self, node):
    items = []
    if node:
      items.append(node.value)
      MISSING CODE
     MISSING CODE
    return items


OPTIONS:
A.

items = items + self.depth_traversal(node.right)
items = items + self.depth_traversal(node.left)


B.

items = items + self.depth_traversal(node.left)
items = items + self.depth_traversal(node.right)


C.

items = items + self.depth_traversal(node.top)
items = items + self.depth_traversal(node.bottom)


D.

items = items + self.depth_traversal(node.start)
items = items + self.depth_traversal(node.end)

Option A
Option B
Option C
Option D
Question 2

You create an instance of the Binary Search Tree and insert the following data. What would be the result of traversing the tree in depth-first order?

node = Node(10)
node.insert(5)
node.insert(25)
node.insert(12)
node.insert(33)
node.insert(18)

[10, 5, 25, 12, 18, 33]
[5, 10, 12, 18, 25, 33]
[10, 5, 25, 12, 33, 18]
[5, 10, 12, 18, 33, 25]
"""
