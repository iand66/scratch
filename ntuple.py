from collections import namedtuple

# Point = namedtuple('Point','x y z')
# P = Point(3,4,5)
# print(P)
# print(P.x, P.y, P.z)
# print(P._asdict())
# print(P._fields)
# P = P._replace(x=6)
# print(P)

# P2 = P._make(['a','b','c'])
# print(P2)

# Tuple - Immutable
color = (55,155,255)
print(color[0])

# Dictionary
color = {'red':55, 'green':155, 'blue':255}
print(color['red'])

# Named Tuple
Color = namedtuple('Color',['red','green','blue'])
color = Color(55,155,255)
print(color[0])
print(color.red)
