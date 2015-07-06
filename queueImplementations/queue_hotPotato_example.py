from queue_implementation import Queue

def hotPotato(namelist, num):
    """
    Hot potato game simulation
    """
    
    q = Queue()
    
    for name in namelist:
        q.enqueue(name)
        
    while q.size() > 1:
        for i in range(num):
            q.enqueue(q.dequeue())
        
        q.dequeue()
        
    return q.dequeue()

# test
print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))
    
        