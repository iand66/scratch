from queue import Queue, LifoQueue, PriorityQueue

q1 = Queue()
q2 = LifoQueue()
q3 = PriorityQueue()

nums1 = [10,20,30,40,50,60,70,80,90]
nums2 = [1,2,3,4,5,6,7,8,9]

for num in nums1:
    q1.put(num)

print(q1.get())
print(q1.get())

for num in nums2:
    q2.put(num)

print(q2.get())
print(q2.get())

q3.put((1, "This is my top priority"))
q3.put((2, "This is the next most important thing"))
q3.put((3, "Maybe this will get done"))
q3.put((99, "It just don't care anymore!"))

while not q3.empty():
    print(q3.get())