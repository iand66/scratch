nums = [1,2,3]
inums = iter(nums)

while True:
    try:
        print(next(inums))
    except StopIteration:
        break