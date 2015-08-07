# basic recursion to calculate sum of a list of integers

def listSum(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + listSum(numList[1:])
    
# test
print(listSum([1, 3, 5, 7, 9]))