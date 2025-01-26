# Queue - Fifo
# Functions
    # push()
    # pop()
    # empty()
    # peek()/top()
    # size()
# used in customers waiting in line, keyboard buffers, LinkedLists, PriorityQueues, BFS

# Implementation using List
queue1 = []
queue1.append('a')
queue1.append('b')
queue1.append('c')
print(queue1.pop(0))
print(queue1)
print('-'*50)

# Implementation using collections.deque()
from collections import deque
queue2 = deque()
queue2.append('a')
queue2.append('b')
queue2.append('c')
print(queue2.popleft())
print(queue2)
print('-'*50)

# Implementation using queue.Queue()
from queue import Queue
queue3 = Queue(maxsize=3)
queue3.put('a')
queue3.put('b')
queue3.put('c')
print(queue3)
print(queue3.full())
print(queue3.empty())
print(queue3.get())
print('-'*50)
