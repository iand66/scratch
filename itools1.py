import itertools

base =  [100,200,300,400]
data = list(zip(itertools.count(), base))
print(data)

toggle = itertools.cycle(['On','Off'])
print(next(toggle))
print(next(toggle))

repeater = itertools.repeat(5, times=3)
for r in repeater:
    print(next(repeater))