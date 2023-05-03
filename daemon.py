import threading, time

path = "textfile.txt"
text = ""

def readfile():
    global path, text
    while True:
        with open(path, "r") as f:
            text = f.read()
        time.sleep(1)

def printit():
    for x in range(30):
        print(x, text)
        time.sleep(1)

t1 = threading.Thread(target=readfile, daemon=True)
t2 = threading.Thread(target=printit)

t1.start()
t2.start()