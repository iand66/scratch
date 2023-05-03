s1 = {1,2,3}
s2 = {2,3,4}
s3 = {3,4,5}

s4 = s1.intersection(s2) # A and B
print(s4)

s4 = s1.intersection(s2, s3)
print(s4)

s4 = s1.difference(s2) # A not B
print(s4)

s4 = s1.symmetric_difference(s2) # A not B
print(s4)

s4 = s3.difference(s1, s2) # A not B
print(s4)