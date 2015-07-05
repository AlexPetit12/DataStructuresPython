from stack_implementation import Stack

def tirpleParenthesesChecker(symbolString):
    """
    Checks whether or not a set of parentheses,
    square brackets and curly braces is correctly balanced
    """
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index = index + 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(opener, closer):
    opens = "([{"
    closers = ")]}"
    return opens.index(opener) == closers.index(closer)

# test
#print(tirpleParenthesesChecker('{{([][])}()}'))
#print(tirpleParenthesesChecker('[{()]'))