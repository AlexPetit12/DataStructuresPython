class Queue:
    """
    Very basic implementation of a queue
    """
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.insert(0, item)
        
    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)

# test
"""
q = Queue()
q.enqueue('hello')
print(q.size())
q.enqueue('dog')
q.enqueue(3)
print(q.dequeue())
print(q.size())
"""