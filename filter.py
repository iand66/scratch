def isOdd(x):
    return x%2 != 0

def isEven(x):
    return x%2 == 0

a = [1,2,3,4,5,6,7,8,9]
b = list(filter(isOdd,a))
c = list(filter(isEven,a))
print(b,c)