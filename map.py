l1 = [1,2,3,4,5,6,7,8,9]

def func(x):
    return x**2

l2 = []
for x in l1:
    l2.append(func(x))

print(l2)

print([func(x) for x in l1])
print(list(map(func, l1)))