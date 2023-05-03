import threading

event = threading.Event()

def function():
    print("Waiting for event trigger")
    event.wait()
    print("Performing XYZ function now")

t1 = threading.Thread(target=function)
t1.start()

x = input("Trigger now? (Y/N)")
if x.upper() == 'Y':
    event.set()