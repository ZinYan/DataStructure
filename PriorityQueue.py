# Priority Queue - Fifo DS that serves high priority elements first
# used in airlines such that First Class or Business class luggages arrive first

# Implementation using list
pqueue1 = []
pqueue1.append((2,'khin'))
pqueue1.append((2,'zin'))
pqueue1.append((1,'yin'))
pqueue1.append((3,'pyay'))
pqueue1.sort()
while pqueue1:
    print(pqueue1.pop(0))
print(len(pqueue1))
print('-'*50)

# Implementation using queue.PriorityQueue()
from queue import PriorityQueue
queue2 = PriorityQueue(maxsize=4)
queue2.put((2,'khin'))
queue2.put((2,'zin'))
queue2.put((1,'yin'))
queue2.put((3,'pyay'))
print(queue2.full())
print(queue2.empty())
while not queue2.empty():
    print(queue2.get())
print('-'*50)

# Implementation using heapq
    # simple scheduler that assigns jobs to the processor
import heapq 
import time
# jobs to be executed 
jobs = [(2, 'task_1'), (5, 'task_2'), (1, 'task_4'), 
        (4, 'task_5'), (3, 'task_3'), (1, 'task_8')] 
  
# interrupts 
interrupts = [(1, 'intr_1'), (2, 'intr_2'), (13, 'intr_3')] 

# Arranging jobs in heap
heapq.heapify(jobs)
j = 0
while len(jobs) != 0:
    # printing execution log
    print(f'{jobs[0][1]} with priority {jobs[0][0]} is in the progress')
    # pop job that completed
    heapq.heappop(jobs)
    if j < len(interrupts):
        # Adding interrupts
        heapq.heappush(jobs,interrupts[j])
        # printing interrupt
        print(f"New interrupt arrived!! {interrupts[j]}")
        j += 1
    print(f'Job Queue: ', jobs)
    print()
print('All jobs and interrupts are completed!!')
