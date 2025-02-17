class LinkedList:
    def __init__(self):
        """Creating a new singly-linked list."""
        self.head = None

    def __repr__(self):
            """Creating a string representation of the data in a list"""
            nodes = []
            curr = self.head
            while curr:
                nodes.append(repr(curr))
                curr = curr.nextval
            return '[' + '->'.join(nodes) + ']'

    def prepend(self, dataval):
        """Insert a new element at the beginning of the list."""
        self.head = Node(dataval=dataval, nextval=self.head)

    def append(self, dataval):
        """Insert a new element at the end of the list."""    
        if not self.head:
            self.head = Node(dataval=dataval)
            return
        curr = self.head
        while curr.nextval:
            curr = curr.nextval
        curr.nextval = Node(dataval=dataval)
               
    def add_after(self, middle_dataval, dataval):
        """Insert a new element after the node with middle_dataval."""     
        if middle_dataval is None:
            print("Data to insert after not specified")
            return
        curr = self.head
        while curr and curr.dataval != middle_dataval:
            curr = curr.nextval
        new_node = Node(dataval = dataval)
        new_node.nextval = curr.nextval
        curr.nextval = new_node

    def find(self, data):
        """Search for the first element with `dataval` matching
        `data`. Return the element or `None` if not found."""
        curr = self.head
        while curr and curr.dataval != data:
            curr = curr.nextval
        return curr  # Will be None if not found

    def remove(self, data):
        """Remove the first occurrence of `data` in the list."""
        # Find the element and keep a
        # reference to the element preceding it
        curr = self.head
        prev = None
        while curr and curr.dataval != data:
            prev = curr
            curr = curr.nextval
        # Unlink it from the list
        if prev is None:
            self.head = curr.nextval
        elif curr:
            prev.nextval = curr.nextval
            curr.nextval = None
            
    def reverse(self):
        """Reverse the list in-place."""
        curr = self.head
        prev_node = None
        next_node = None
        while curr:
            nextval = curr.nextval
            curr.nextval = prev_node
            prev_node = curr
            curr = nextval   
        self.head = prev_node

    def reverse_recursive(self):
        """Reverse the list in place using recursion"""
        def recursion(curr, prev):
            if not curr:
                return prev
            nextval = curr.nextval
            curr.nextval = prev
            prev = curr
            curr = nextval
            return recursion(curr, prev)
        # update the head of the original linked list 
        self.head = recursion(curr=self.head, prev=None)
        
    def count_nodes(self):
        """Count the number of nodes in the linked list."""
        if (self.head  == None): 
            return  0
        else: 
            curr = self.head
            count = 0
            while (curr != None):
                curr = curr.nextval
                count += 1            
        return count