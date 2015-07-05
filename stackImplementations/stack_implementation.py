class Stack:
    """
    Very basic implementation of a stack
    """
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)

# test
"""
s = Stack()
print(s.isEmpty())
s.push(15)
print(s.peek())
s.push('Hello')
print(s.peek())
print(s.size())
print(s.pop())
print(s.peek())
"""