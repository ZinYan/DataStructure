# Without multithreading
import time
def square_nums(arr):
    print('Calculate square numbers: ')
    for i in arr:
        time.sleep(0.2)
        print(f'square: {i*i}')
def cube_nums(arr):
    print('Calculate cubic numbers: ')
    for i in arr:
        time.sleep(0.2)
        print(f'cube: {i*i*i}')

arr = [2,4,6,8]

t = time.time()
square_nums(arr)
cube_nums(arr)
total_time = time.time() - t
print(f'total time :{total_time}')

# With Multithreading
import time
import threading 

def square_nums(arr):
    print('Calculate square numbers: ')
    for i in arr:
        time.sleep(0.2)
        print(f'square: {i*i}')
def cube_nums(arr):
    print('Calculate cubic numbers: ')
    for i in arr:
        time.sleep(0.2)
        print(f'cube: {i*i*i}')

arr = [2,4,6,8]

t = time.time()
th1 = threading.Thread(target=square_nums,args=(arr,))
th2 = threading.Thread(target=cube_nums,args=(arr,))

# Start branching from main thread
th1.start()
th2.start()

# Rejoining to the main thread
th1.join()
th2.join()

total_time = time.time() - t
print(f'total time :{total_time}')