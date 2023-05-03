import threading, time

sem = threading.BoundedSemaphore(value=5)

def access(number):
    print(f"{number} is accessing")
    sem.acquire()
    print(f"{number} acquired access")
    time.sleep(2)
    print(f"{number} is now releasing")
    sem.release()

for num in range(1,11):
    t= threading.Thread(target=access, args=(num,))
    t.start()
    time.sleep(1)
