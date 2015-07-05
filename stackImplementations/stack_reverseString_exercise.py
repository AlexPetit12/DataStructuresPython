from stack_implementation import Stack

def revString(myStr):
    """
    Reverses a String
    """
    
    s = Stack()
    
    for c in myStr:
        s.push(c)
        
    newStr = ""
    
    while not s.isEmpty():
        newStr += s.pop()
        
    return newStr

# test
#print(revString("hello"))