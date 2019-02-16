import threading
import time

def printHello():
    for x in range(1, 100):
        print("mythread: " + str(x))

mythread = threading.Thread(target=printHello)
mythread.start()

for x in range(1, 100):
    print("mainthread" + str(x))
