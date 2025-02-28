# Queue - Fifo
# Functions
    # push()
    # pop()
    # empty()
    # peek()/top()
    # size()
# used in customers waiting in line, keyboard buffers, LinkedLists, PriorityQueues, BFS

'''
Producer(New York Stock Exchange) supply stock data to consumer(organizations like Yahoo Finance, Google Finance etc).
Without Queue
    - when http server of organizations is down, there will be loss of data
    - managing multiple consumers become problematic
With Queue
Producer put stock data to queue & consumer receive data in the order that they were pushed
Producer -> Queue(data3, data2, data1) -> Consumer

Implementations
    Python
        list
        collections.deque
        queue.LifoQueue
    Java
        LinkedList
    C++ 
        std::queue
'''

# Using List
wmt_stock_price_queue = []
# Keep inserting in front(0)
wmt_stock_price_queue.insert(0,131.10)
wmt_stock_price_queue.insert(0,132.12)
wmt_stock_price_queue.insert(0,135)
# 135, 132,12, 131,10
# 1st element pushed
print(wmt_stock_price_queue.pop())

# Using collections.deque
from collections import deque
q = deque()
q.appendleft(131.10)
q.appendleft(132.12)
q.appendleft(135)
print(q.pop())

# Queue Class using deque
class Queue:
    def __init__(self):
        self.queue = deque()
    def enqueue(self,value):
        self.queue.appendleft(value)
    def dequeue(self):
        if self.size() == 0:
            print("Queue is empty")
            return
        return self.queue.pop()
    def peek(self):
        return self.queue[-1]
    def is_empty(self):
        return self.queue==0
    def size(self):
        return len(self.queue)

stock_queue = Queue()
stock_queue.enqueue({
    'company' : 'Wal Mart',
    'timestamp' : '15 apr, 11.01 AM',
    'price' : 131.10
})
stock_queue.enqueue({
    'company' : 'Wal Mart',
    'timestamp' : '15 apr, 11.02 AM',
    'price' : 132.12
})
stock_queue.enqueue({
    'company' : 'Wal Mart',
    'timestamp' : '15 apr, 11.05 AM',
    'price' : 135
})
print(stock_queue.queue)
# 1st data that got pushed
print(stock_queue.dequeue())
print(stock_queue.peek())


# Food ordering system
import time 
import threading
order_queue = Queue()
# Placing new order every 0.5 sec
def place_order(orders):
    for food in orders:
        print(f'Placing order for: {food}')
        order_queue.enqueue(food)
        time.sleep(0.5)

# Serving an order every 2 sec
def serve_order():
    time.sleep(1)
    while order_queue.size()!=0:
        order = order_queue.dequeue()
        print(f'Now serving: {order}')
        time.sleep(2)

if __name__ == '__main__':
    orders = ['pizza','samosa','pasta','biryani','burger']
    th1 = threading.Thread(target=place_order,args=(orders,))
    th2 = threading.Thread(target=serve_order)

    th1.start()
    th2.start()

    th1.join()
    th2.join()

# Print binary nums from 1 to 10
'''
1
10 [1st num(1) + 0]
11 [1st num(1) + 1]
100 [2nd num(10) + 0]
101 [2nd num(10) + 1]
110 [3rd num(11) + 0]
111 [3rd num(11) + 1]
1000 [4th num(100) + 0]
1001 [4th num(100) + 1]
1010 [5th num(101) + 0]
'''
def produce_binary_nums(n):
    binary_numQueue = Queue()
    binary_numQueue.enqueue('1')
    for i in range(n):
        num = binary_numQueue.peek()
        print(num)
        binary_numQueue.enqueue(num + '0')
        binary_numQueue.enqueue(num + '1')
        binary_numQueue.dequeue()
if __name__ == '__main__':
    produce_binary_nums(10)


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


