from deque_implementation import Deque

def palindromeChecker(s):
    """
    Checks whether or not a string is a palindrome
    """
    d = Deque()
    
    for c in s:
        d.addRear(c)
        
    equal = True
    
    while d.size() > 1 and equal:
        first = d.removeFront()
        last = d.removeRear()
        if first != last:
            equal = False
            
    return equal

# test
#print(palindromeChecker("Eric"))
#print(palindromeChecker("madam"))
        
        
    