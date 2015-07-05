from stack_implementation import Stack

def parenthesesChecker(symbolString):
    """
    Checks whether or not a set of parentheses is correctly balanced
    """
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

# test
#print(parenthesesChecker('((()))'))
#print(parenthesesChecker('(()'))