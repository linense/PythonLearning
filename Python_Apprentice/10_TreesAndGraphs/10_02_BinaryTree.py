class Node:

    def __init__(self, data): #Constructor
        self.left = None # initialize the left son to none
        self.right = None # initialize the right son to none
        self.data = data
        
    def get_left_child(self):
        return self.left
    
    def set_left_child(self, left):
        self.left = left
    
    def get_right_child(self):
        return self.right
    
    def set_right_child(self,right):
        self.right = right
    
    def get_value(self): # get the value of the current node
        return self.data

    def set_value(self, value):
        self.data = value
        
    def print_tree(self): # performs some kind of in-order traversal by recursively calling the functions
            if self.left: # Is there a left child? If yes, print it out
                self.left.print_tree() 

            print(self.data)

            if self.right:
                self.right.print_tree()

class MyQueue:
    
    def __init__(self):
        """ Create a new queue."""
        self.items = []

    def is_empty(self):
        """ Returns true if queue is empty """  
        return len(self.items) == 0

    def enqueue(self, item):
        """ Add a new element to the end of queue."""
        self.items.append(item)

    def dequeue(self):
        """ Remove a element from the beginning of queue."""
        return self.items.pop(0)

    def size(self):
        """ Returns the size of the queue."""
        return len(self.items)
    
    def peek(self):
        """ Have a look at first element of the queue."""
        if self.is_empty():
            raise Exception("Nothing to peek")
        return self.items[0]

def insert(head, node):
    
    if head == None: # checks if the current sub-tree is empty. It then becomes a new leaf
        return node
    
    if node.get_value() <= head.get_value():
        head.set_left_child(insert(head.get_left_child(), node))
    else:
        head.set_right_child(insert(head.get_right_child(), node))
        
    return head

def lookup(head, data):
    
    if head == None:
        return print("Value not found!")
    
    if head.get_value() == data:
        return head
    
    if data <= head.get_value():
        return lookup(head.get_left_child(), data)
    else:
        return lookup(head.get_right_child(), data)
    
def print_node(node):
    if (node == None): 
        print("Not found!")
    
    print(node.get_value())

def min_value(head): 
    current = head 
 
    # loop down to find the leftmost leaf
    while(current.left != None): 
        current = current.left  
  
    return current.data

def max_value( head): 
    current = head 
  
    # loop down to find the rightmost leaf 
    while(current.right != None): 
        current = current.right
  
    return current.data

def breadth_first(node):
        
    if (node == None):
        raise Exception("No root found!")
    path = [] 
    queue = MyQueue()
    queue.enqueue(node)
    while queue.size() > 0:        
        current = queue.dequeue()       
        path.append(current.data)             
        if current.get_left_child() != None:
            queue.enqueue(current.get_left_child())           
        if current.get_right_child() != None:
            queue.enqueue(current.get_right_child())
    return path

def pre_order(node): 
    path = []
    if node:
        path.append(node.data)
        path = path + pre_order(node.get_left_child())
        path = path + pre_order(node.get_right_child())
    return path

def in_order(node): 
    path = []
    if node:       
        path = path + in_order(node.get_left_child())
        path.append(node.data)
        path = path + in_order(node.get_right_child())
    return path

def post_order(node): 
    path = []
    
    if node:       
    
        path = path + post_order(node.get_left_child())        
        path = path + post_order(node.get_right_child())
        
        path.append(node.data)

    return path

A = Node(45)
B = Node(2)
C = Node(33)
D = Node(54)
E = Node(25)
F = Node(68)
G = Node(72)
H = Node(81)
I = Node(23)

head = insert(None, E)
#head.print_tree()

insert(head, B)
#head.print_tree()
insert(head, C)
#head.print_tree()
insert(head, I)
insert(head, A)
#head.print_tree()
insert(head, G)
insert(head, F)
insert(head, D)
insert(head, H)
#head.print_tree()
#print_node(lookup(head, 68))
#print_node(lookup(head, 10))
#print(min_value(head))
insert(head, Node(1))
#print(min_value(head))

insert(head, Node(100))
#print(max_value(head))

#print(breadth_first(E))

print(pre_order(E))
print(in_order(E))
print(post_order(E))