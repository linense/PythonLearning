# Create a graph class that implements an adjacency matrix
class Graph:
  def __init__(self, size):
    self.m = []
    for _ in range(size):
      self.m.append([0] * size)
    self.size = size

# Implement a method to add an edge to the graph
  def add(self, v, w):
    if v == w:
      raise ValueError('Cannot add an edge to itself.')
    self.m[v][w] = 1
    self.m[w][v] = 1

# Implement a method to remove an edge from the graph
  def remove(self, v, w):
    if self.m[v][w] == 0:
      return
    self.m[v][w] = 0
    self.m[w][v] = 0

# Implement a method to display the contents of the matrix
  def __str__(self):
    retval = ''
    for i in self.m:
      for j in i:
        retval += f'{j}\t'
      retval += '\n'
    return retval

# Construct a graph and display its contents
graph = Graph(6)
graph.add(0, 3)
graph.add(1, 4)
graph.add(2, 5)
graph.add(0, 5)
print(graph)   

"""
Introduction

Welcome to the Graphs as an Adjacency Matrix Python Lab. Your assignment for this exercise is to implement a graph as an adjacency matrix in Python and to answer the assessment questions
Task

    Implement a graph as an adjacency matrix in Python

    Create a graph class that implements an adjacency matrix
    Implement a method to add an edge to the graph
    Implement a method to remove an edge from the graph
    Implement a method to display the contents of the matrix
    Construct a graph and display its contents

Instructions
Task 1 - Create a graph class that implements an adjacency matrix

    The first step in the exercise is to create a graph class that implements an adjacency matrix. On line 2, we have a class graph. And in this graph, define a __init__ method that takes self and size as parameters. Inside the body of the class graph, define a __init__ method that defines a single parameter size. It's going to be a square matrix of the given size, its size by size. Define the matrix, self.m equals the double brackets. These square brackets define a list. It's going to be a list of lists to define our adjacency matrix.

    And then for _ in range(size), so we don't need the loop variable, so I just put it as an underscore and we loop size times. We're going to do self.m.append, and we're going to have 0 array times size. This is an adjacency matrix that's initialized to all zeros. Then self.size = size.

# Create a graph class that implements an adjacency matrix
class Graph:
  def __init__(self, size):
    self.m = []
    for _ in range(size):
      self.m.append([0] * size)
    self.size = size

Task 2 - Implement a method to add an edge to the graph

    Now we need to implement a method to add an edge to the graph. It's to set the appropriate cell in our matrix to be 1 to designate an edge. The parameters that define the nodes are v and w. On line 11, We check to see that v = w. If it is, then we raise a ValueError saying that we cannot add an edge to itself. Then we set, self.m of vw, so we're indexing at v and w equal to 1, and we need to set self.m[w][v] = 1. So an edge from one node to another and back so that edge is complete.

# Implement a method to add an edge to the graph
  def add(self, v, w):
    if v == w:
      raise ValueError('Cannot add an edge to itself.')
    self.m[v][w] = 1
    self.m[w][v] = 1

Task 3 - Implement a method to remove an edge from the graph

    If there's an edge from node v to w, there's automatically an edge from w to v. Now we need to implement a method to remove an edge from the graph. We define a remove function that specifies v and w. Now if self.m[v][w] is already equal to 0, so if there's no edge, then we can just skip the removal. Otherwise, we set self.m at v and w equal to 0 and at w and v equal to 0.

# Implement a method to remove an edge from the graph
  def remove(self, v, w):
    if self.m[v][w] == 0:
      return
    self.m[v][w] = 0
    self.m[w][v] = 0

Task 4 - Implement a method to display the contents of the matrix

    We need to implement a method to display the contents of the matrix. Overload the special string method the __str__ method, so that we can do a print on the graph instance and it will print the contents. Define this, and then in the body of this method, we have retval equals an empty string.

    We start with an empty string, then for i in self.m:, so we loop over m, and we do it for j in i. So i will be a list, since m is the list of lists. In the inner list, we have for j in i:, and then we set retval plus equals the formatted string of the node value. Whether it's a 1 or 0, so that will be contained in j and then a tab character, so we separate each cell by a tab. And then retval += \n. So after each row, we start a new row on a new line, so that's why we need the newline character. And then in the end, we return retval, which should be our constructed string with the contents of the matrix.

# Implement a method to display the contents of the matrix
  def __str__(self):
    retval = ''
    for i in self.m:
      for j in i:
        retval += f'{j}\t'
      retval += '\n'
    return retval

Task 5 - Construct a graph and display its contents

    Then the next step is to construct a graph and display its contents. Set the graph, all in lowercase equal to the graph class with the uppercase G, and we set it to be 6. This is a size of 6, so it's a 6 by 6 graph, which means it has 6 nodes and the nodes are enumerated from 0 to 5. We do graph.add(0, 3). So there's an edge from 0 to 3 and 3 to 0. And then graph.add(1, 4), graph.add(2, 5) and graph.add(0, 5). This constructs a graph with the edges as we defined here. And then we just call print graph, which calls the string function we defined above.

# Construct a graph and display its contents
graph = Graph(6)
graph.add(0, 3)
graph.add(1, 4)
graph.add(2, 5)
graph.add(0, 5)

print(graph)

Terminal

    Now we run the code, so we can see the results. And here we get our graph, so we have each row. So enumerated from 0, 0, 1, 2, 3, 4, 5. In this case if we go along the row from 0, 1, 2, 3, so this particular one is in the 0 row and the third column. If we're calling from 0 to 0 row and column 3, so that's our graph node from 0 to 3. And then the final one in the first row is our edge from 0 to 5.

    Then in the next row, we have our edge from 1 to 4, and then our edge from 2 to 5 in the next row. Now in the bottom part, you'll notice that if you draw a line down the middle of the graph, down the diagonal, this graph is symmetrical. And it will always be symmetrical because it's an un-directed graph, which means if there's a node from 0 to 3, there's automatically a node from 3 to 0. And that concludes this exercise.

terminal_app_07.png
Check your work

Check each box to confirm completion of the task.

    Create a graph class that implements an adjacency matrix
    Implement a method to add an edge to the graph
    Implement a method to remove an edge from the graph
    Implement a method to display the contents of the matrix
    Construct a graph and display its contents

Question 1

Which of the following would complete the code to add an edge to a graph that implements an adjacency matrix?

def add(self, v, w):
    if v == w:
      raise ValueError('Cannot add an edge to itself.')
    MISSING CODE
    MISSING CODE


OPTIONS:
A.

self.m(v)*(w) = 1
self.m(w)*(v) = 1


B.

self.m(v)(w) = 1
self.m(w)(v) = 1


C.

self.m[v]*[w] = 1
self.m[w]*[v] = 1


D.

self.m[v][w] = 1
self.m[w][v] = 1

Option A
Option B
Option C
Option D
Question 2

Which of the following would complete the code to display the contents of the matrix?

  def __str__(self):
    retval = ''
    for i in self.m:
      for j in i:
        MISSING CODE
      retval += '\n'
    return retval

retval += f'{i}\t'
retval -= f'{j}\t'
retval += f'{j, I }\t'
retval += f'{j}\t'
"""