# Stack - Lifo
# Functions
    # push()
    # pop()
    # empty()
    # peek()/top()
    # size()
# used in undo/redo features, call functions, backtracking algorithms

# Implementation using List
stack1 = []
stack1.append('a')
stack1.append('b')
stack1.append('c')
print(stack1)

print(stack1.pop())
print('-'*50)

# Implementation using collections.deque
from collections import deque
stack2 = deque()
stack2.append('a')
stack2.append('b')
stack2.append('c')
print(stack2)

print(stack2.pop())
print('-'*50)

# Implementation using queue.LifoQueue()
from queue import LifoQueue
stack3 = LifoQueue(maxsize=3)
stack3.put('a')
stack3.put('b')
stack3.put('c')
print(stack3)
print(stack3.qsize())
print(stack3.full())
print(stack3.empty())
print(stack3.get())
print('-'*50)

# Implementation using a singly linked list
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class Stack:
    # This is called a dummy node that does not include in calculation but make it easier
    def __init__(self):
        self.head = Node("head")
        self.size = 0
    # String representation of the stack
    def __str__(self):
        # cur = stack.head.next (Node instance with value 5 & next->Node instance with value 4)
        cur = self.head.next
        out = ""
        while cur:
            # out += Node instance with value 5.value ->
            out += str(cur.value) + '->'
            # cur = Node instance with value 4 
            cur = cur.next
        # return except last -(-2) and >(-1)
        return out[:-2]
    # Push a value into the stack
    def push(self,value):
        # create a node
        node = Node(value)
        # make created node point to the current head
        node.next = self.head.next
        # update the head to be the new node
        self.head.next = node
        self.size +=1
    def isEmpty(self):
        return self.size==0
    def pop(self):
        if self.isEmpty():
            raise Exception("The stack is Empty!!")
        remove = self.head.next
        self.head.next = remove.next
        self.size -= 1
        return remove.value
    def getSize(self):
        return self.size
    def peek(self):
        if self.isEmpty():
            return None
        return self.head.next.value 
if __name__ == '__main__':
    # create a Stack instance (self=stack)
        # self.head -> Node instance 
            # create Node instance (self=stack.head)
                # self.value = "head"
                # self.next = None
        # self.size = 0
    stack = Stack()
    for i in range(1,6):
        # i = 1
            # create Node instance (self=node)
                # self.value = 1
                # self.next = None
            # make created node point to the current head
                # node.next -> stack.head.next(None)
            # update the head to be the new node
                # stack.head.next(next of Node instance with value "head") -> node(Node instance with value=1,next=None)
            # add size
                # stack.size +=1
        # i = 2
            # create Node instance (self=node)
                # self.value = 2
                # self.next = None
            # make created node point to the current head
                # node.next -> stack.head.next(Node instance with value=1 next=None)
            # update the head to be the new node
                # stack.head.next(next of Node instance with value 1) -> node(Node instance with value=2,next->Node instance with value=1,next=None)
            # add size
                # stack.size +=1
        stack.push(i)
    # print according to its string representation
    print(f'Stack: {stack}')
    print(f'Stack size: {stack.getSize()}')
    # stack.head.next.value (stack.head -> [Node instance with value "head" and next->Node instance with value 5])
    print(f'Peek top value: {stack.peek()}')
    for _ in range(1,3):
        # i = 1
            # remove = stack.head.next(Node instance with value=5)
            # stack.head.next -> remove.next(Node instance with value 4)
            # stack.size -= 1
            # remove.value (Node instance with value 5.value)
        top_value = stack.pop()
        print(f'Pop value: {top_value}')
    print(f'Stack: {stack}')
print('-'*50)
