from collections import Counter

c = Counter('Gallad')
print(c) # 2xa 2xl 1xG 1xd

c = Counter(['a','a','b','c','c'])
print(c) # 2xa 2xc 1xb

c = Counter({'a':1, 'b':2})
print(c) # 2xb 1xa

c = Counter(cats=4, dogs=7)
print(c) # dogsx7 catsx4
print(list(c.elements()))
print(c.most_common(2))

c = Counter(a=4, b=2, c=0, d=2)
print(c)
d = ['a','b','b','c']
c.subtract(d) # Subtract count of d from c
print(c)
c.update(d) # Add count of d to c
print(c)