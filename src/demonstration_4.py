# class LinkedListNode:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.appenjd(item)
    
    def pop(self):
        if len(self.items) == 0:
            return None
        last_item = self.items.pop()
        return last_item