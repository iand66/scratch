import itertools

letters = ['a','b','c','d']
numbers = [0,1,2,3]
names = ['Ian', 'Jeanette', 'Pedro', 'Ellie']

# result = itertools.combinations(letters,2)
# for r in result:
#     print(r)

# result = itertools.permutations(letters,2)
# for r in result:
#     print(r)

result = itertools.product(numbers, repeat=3)
for r in result:
    print(r)