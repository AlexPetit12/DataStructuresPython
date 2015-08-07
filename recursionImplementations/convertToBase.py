# convert an int to a different base

def convert(n, base):
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return convert(n // base, base) + convertString[n % base]

# test  
print(convert(100, 16))