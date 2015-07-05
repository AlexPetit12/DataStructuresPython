from stack_implementation import Stack

def baseConverter(n, base):
    """
    Returns a decimal number into another base between 1 and 16
    """
    
    digits = "0123456789ABCDEF"
    
    s = Stack()
    
    while n != 0:
        reminder = n % base
        s.push(reminder)
        n = n / base
        
    baseString = ""
    
    while not s.isEmpty():
        baseString += digits[s.pop()]
        
    return baseString

# test
#print(baseConverter(25, 2))
#print(baseConverter(256, 16))