'''
Arrays
    Dynamic array: 
        Capacity : original capacity = 5 -> if capacity is full, you have to allocate memory for 5*2=10 + original 5 => 15 again and copy original 5 into that space which is not efficient
        Insertion, Deletion : takes O(n)
    Time Complexity:
        Indexing : O(1)
        Insert/Delete element at start : O(n)
        Insert/Delete element at end : O(1) (but if you have dynamic array and you have to copy as you reach full capacity, there will be additional cost)
        Insert element in middle O(n)
Linked List
    stores address of next element
    (A,addressofB) -> (B,addressofC) -> (C,null)
    Time Complexity:
        Indexing : O(n)
        Insert/Delete element at start : O(1)
        Insert/Delete element at end : O(n) (have to traverse till the end)
        Insert element in middle : O(n) (have to traverse)
        Linked List Traversal : O(n)
    Adv over array
        Don't need to preallocate space
        Insertion is easier
Doubly Linked List
    store address of both previous and next element
    (null,A,addressofB) -> (addressofB,B,addressofC) -> (addressofB,C,null)
'''
class Node: 
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

# Head -> (A,addressofB) -> (B,addressofC) -> (C,null)
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_start(self,data):
        # Head -> (newNode,addressofA) -> (A,addressofB) ->(B,addressofC) -> (C,null)
        node = Node(data,self.head)
        self.head = node
    def print(self):
        # Empty list
        if self.head is None:
            print('Linked List is empty.')
            return
        
        itr = self.head
        ll = ''
        while itr:
            ll += itr.data + '->'
            itr = itr.next
        print(ll[:-2])
    def insert_at_end(self,data):
        # Head -> (A,addressofB) ->(B,addressofC) -> (C,addressofnewNode) -> (newNode,null)
        # if list is empty, 
        if self.head is None:
            self.head = Node(data,None)
            return
        node = Node(data,None)
        itr = self.head
        while itr.next:
            itr = itr.next
        # itr will contain last element at the end of the loop
        itr.next = node
    def new_linkedList(self,data_list):
        # data_list = ['orange','banana','mango','kiwi']
        # Head -> (orange,addressofbanana) -> (banana,addressofmango) -> (mango,addressofkiwi) -> (kiwi,null)
        self.head = None #to wipe out all existing values
        for data in data_list:
            self.insert_at_end(data)
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            count += 1
        return count
    def remove_at(self,index):
        # Head -> (orange,addressofbanana) -> (banana,addressofmango) -> -> (kiwi,null)
        # if index is negative or out of range
        if index<0 or index>=self.get_length():
            raise Exception("Invalid index!!")
        # if index to be removed is 1st element -> no need to traverse(iterate)
        if index==0:
            self.head = self.head.next
            return
        itr = self.head
        count = 0
        while itr:
            if count == index-1:
                itr.next = itr.next.next 
                break
            itr = itr.next
            count += 1
    def insert_at(self,index,data):
        # Head -> (orange,addressofgrapes) ->  (grapes,addressofbanana) -> (banana,addressofkiwi) -> (kiwi,null)
        # if index is negative or out of range
        if index<0 or index>self.get_length():
            raise Exception("Invalid index!!")
        if index == 0:
            self.insert_at_start(data)
            return
        if index == self.get_length():
            self.insert_at_end(data)
            return
        itr = self.head
        count = 0
        while itr:
            if count == index-1:
                node = Node(data,itr.next)
                itr.next = node 
                break
            itr = itr.next
            count += 1
    def insert_after_value(self, data_after, data_to_insert):
        # Search for first occurance of data_after value in linked list
        # Now insert data_to_insert after data_after node

        # Head -> (orange,addressofgrapes) ->  (grapes,addressofbanana) -> (banana,addressofkiwi) -> (kiwi,null)
        # data_after = orange
        # data_to_insert = strawberry
        # Head -> (orange,addressofstrawberry) -> (strawberry,addressofgrapes) -> (grapes,addressofbanana) -> (banana,addressofkiwi) -> (kiwi,null)
        
        # if linked list is empty
        if self.head is None:
            return
        
        # if 1st element is data_after
        if self.head.data == data_after:
            node = Node(data_to_insert,self.head.next)
            self.head.next = node
            return
        
        itr = self.head 
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert,itr.next)
                itr.next = node
                break
            itr = itr.next

# add breakpoint at the start of the place where you want to debug
if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_start('C')
    ll.insert_at_start('B')
    ll.insert_at_start('A')
    ll.insert_at_end('D')
    ll.print()
    ll.new_linkedList(['orange','banana','mango','kiwi'])
    ll.print()
    print("length:",ll.get_length())
    ll.remove_at(2) # remove mango
    ll.print()
    ll.insert_at(1,"grapes")
    ll.print()
    ll.insert_after_value("orange","strawberry")
    ll.print()
