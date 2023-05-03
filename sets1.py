s1 = set([1,2,3,4,5,4,3,2,1]) # Removes Duplicates
print(s1)

s2 = {1,2,3,4,5}
s2.add(6)
s2.update([7,8,9])
print(s2)

s2.remove(5)
print(s2)
s2.discard(5) # No key value error
print(s2)