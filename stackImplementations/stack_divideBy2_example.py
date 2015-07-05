from stack_implementation import Stack

def divideBy2(n):
    """
    Returns the binary form of a decimal number
    """
    
    s = Stack()
    
    while n != 0:
        reminder = n % 2
        s.push(reminder)
        n = n / 2
        
    binaryString = ""
    
    while not s.isEmpty():
        binaryString += str(s.pop())
        
    return binaryString

# test
print(divideBy2(233))