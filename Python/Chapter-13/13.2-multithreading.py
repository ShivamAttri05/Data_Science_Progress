# Multithreading
# When to use multithreading
# I/O bound tasks: Tasks that spend more time waiting for I/O operations.
# Concurrent Execution: When you want to improve the thoughtput of your application by performing multiple operation concurrently.

import threading
import time

def printNum():
    for i in range(5):
        time.sleep(2)
        print(f"Number: {i}")

def printLet():
    for letter in 'abcde':
        time.sleep(2)
        print(f"Letters: {letter}")

# Create 2 thread
t1 = threading.Thread(target=printNum)
t2 = threading.Thread(target=printLet)

t = time.time()
# Start the thread
t1.start()
t2.start()

# Waiting for the thread to complete
t1.join()
t2.join()

finishedTime = time.time() - t
print(finishedTime)