'''
Stack - Lifo
Functions
    push()
    pop()
    empty()
    peek()/top()
    size()
used in undo/redo features, call functions, backtracking algorithms

Time Complexity 
    Push/Pop element : O(1)
    Search element by value : O(n)
Applications
    Undoing (cmd+Z)
    function calling in any programming language
Implementations
    Python
        list
            not recommended cuz if the capacity is full, have to allocate another memory and copy existing elements which is not efficient
        collections.deque
        queue.LifoQueue
    Java
        Stack
        Deque
    C++
        std::stack
'''

# Using list
stack = []
stack.append('https://www.wikipedia.org/')
stack.append('https://en.wikipedia.org/wiki/Running_Man_(TV_program)')
stack.append('https://en.wikipedia.org/wiki/List_of_Running_Man_episodes_(2010)')
stack.append('https://en.wikipedia.org/wiki/List_of_Running_Man_episodes_(2011)')
print(stack.pop()) # delete and show last added link
print(stack[-1]) # show last added link

# Using coolections.deque
from collections import deque
stack1 = deque()
print(dir(stack1))  # viewing methods
stack1.append('https://www.wikipedia.org/')
stack1.append('https://en.wikipedia.org/wiki/Running_Man_(TV_program)')
stack1.append('https://en.wikipedia.org/wiki/List_of_Running_Man_episodes_(2010)')
stack1.append('https://en.wikipedia.org/wiki/List_of_Running_Man_episodes_(2011)')
print(stack1.pop())

# Stack Class using deque
class Stack:
    def __init__(self):
        self.stack = deque()
    def push(self,value):
        self.stack.append(value)
    def pop(self):
        return self.stack.pop()
    def peek(self):
        return self.stack[-1]
    def is_empty(self):
        return len(self.stack)==0
    def size(self):
        return len(self.stack)

# Reversing string using stack
def reverse_string(str):
    stack = Stack()
    for char in str:
        stack.push(char)
    new_s = ''
    for _ in range(stack.size()):
        new_s += stack.pop()
    return new_s
if __name__ == "__main__":
    print(reverse_string("We will conquer COVID-19"))

# Checking if parentheses are balanced or not using stack
def match(ch,s):
    m = {
        '[' : ']',
        '{' : '}',
        '(' : ')'
    }
    return m[s] == ch
def is_balanced(str):
    s = Stack()
    # ({a+b})
    # ({ -> push
    # } -> pop
    for ch in str:
        if ch == '[' or ch == '{' or ch == '(':
            s.push(ch)
        elif ch == ']' or ch == '}' or ch == ')':
            if s.is_empty():
                return False
            if not match(ch,s.pop()):
                return False
    return s.is_empty()
if __name__ == "__main__":
    print(is_balanced("({a+b})"))
    print(is_balanced("))((a+b}{"))
    print(is_balanced("((a+b))"))
    print(is_balanced("))"))
    print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))


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


