"""
You've encountered a situation where you want to easily be able to pull the
largest integer from a stack.

You already have a `Stack` class that you've implemented using a dynamic array.

Use this `Stack` class to implement a new class `MaxStack` with a method
`get_max()` that returns the largest element in the stack. `get_max()` should
not remove the item.

*Note: Your stacks will contain only integers. You should be able to get a
runtime of O(1) for push(), pop(), and get_max().*
"""

class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        # initialize an empty stack
        self.top = None

    def push(self, item):
        # create a new LL node
        new_node = LinkedListNode(item)
        # point new node to the current top of the stack
        new_node.next = self.top
        # set the TOP variable to the new node
        self.top = new_node

    def pop(self):
        
        # If the stack is empty, return None
        if self.top is None:
            return None
        
        old_top = self.top
        self.top = old_top.next
        
        # optional to sever the connection to the old node
        old_top.next = None

        return old_top.data

    def peek(self):
        """Return the last item without removing it"""
        if not self.items:
            return None
        return self.items[-1]

class MaxStack:
    def __init__(self):
        # Your code here


    def push(self, item):
        """Add a new item onto the top of our stack."""
        # Your code here


    def pop(self):
        """Remove and return the top item from our stack."""
        # Your code here


    def get_max(self):
        """The last item in maxes_stack is the max item in our stack."""
        # Your code here

