from collections import deque

d = deque('Hello')
print(d)

d.extend('World')
print(d)

d.append('s')
print(d)
d.appendleft('X')
print(d)

d.pop() # Remove last element
d.popleft() # Remove first element
print(d)

d.clear()
print(d)

d.extendleft('eroM') # Extends Left -> Right
print(d)

d.rotate(1) # Shift x position Right
print(d)
d.rotate(-1) # Shift x position Left
print(d)

e = deque('HelloWorld', maxlen=10)
print(e, e.maxlen)
e.append('s') # Drops 1st position to maintain maxlen
print(e)
