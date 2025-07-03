# Process that run in parallel
# CPU Bound Tasks - Tasks that are heavy on CPU usage.
# Parallel Execution - Multiple cores of the CPU

import multiprocessing
import multiprocessing.process
import time

def squareNum():
    for i in range(5):
        time.sleep(1.5)
        print(f'Square: {i*i}')

def cubeNum():
    for i in range(5):
        time.sleep(1.5)
        print(f'Cube: {i*i*i}')

if __name__ == "__main__":

    p1 = multiprocessing.Process(target=squareNum)
    p2 = multiprocessing.Process(target=cubeNum)

    p1.start()
    p2.start()

    p1.join()
    p2.join()