class Node:
    def __init__(self,prev=None,data=None,next=None):
        self.data = data
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def insert_at_start(self,data):
        # Head -> (null,A,addressofB) -> (addressofB,B,addressofC) -> (addressofC,C,null)
        node = Node(None,data,self.head)
        if self.head is not None:
            self.head.prev = node
        self.head = node
    def insert_at_end(self,data):
        # Head -> (null,A,addressofB) -> (addressofB,B,addressofC) -> (addressofC,C,null)
        if self.head is None:
            self.head = Node(None,data,None)
            return
        last_node = self.get_last_node()
        last_node.next = Node(last_node,data,None)
    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr
    def new_Linked_List(self,data_list):
        # Wipe out existing data and create new list
        # Head -> (null,orange,addressofbanana) -> (addressoforange,banana,addressofmango) -> (addressofbanana,mango,null)
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def print_forward(self):
        if self.head is None:
            print("Linked List is Empty.")
            return
        itr = self.head
        ll = ''
        while itr:
            ll += itr.data + '->'
            itr = itr.next
        print(ll[:-2])
    def print_backward(self):
        if self.head is None:
            print("Linked List is Empty.")
            return
        itr = self.get_last_node()
        ll = ''
        while itr:
            ll += itr.data + '->'
            itr = itr.prev
        print(ll[:-2])
    def get_length(self):
        itr = self.head
        count = 0
        while itr:
            itr = itr.next
            count += 1
        return count
    def insert_at(self,index,data):
        # Head -> (null,orange,addressofbanana) -> (addressoforange,banana,addressofgrapes) -> (addressofbanana,grapes,addressofmango) ->(addressofgrapes,mango,null)
        if index<0 or index>self.get_length():
            raise Exception('Invalid Index')
        if index == 0:
            self.insert_at_start(data)
            return
        itr = self.head
        count = 0
        while itr:
            if count == index-1:
                node = Node(itr,data,itr.next)
                if node.next:
                    node.next.prev = node
                itr.next = node
                break
            count += 1
            itr = itr.next   
    def remove_at(self,index):
        # Head -> (null,orange,addressofbanana) -> (addressoforange,banana,addressofmango) -> [] ->(addressofbanana,mango,null)
        if index<0 or index>=self.get_length():
            raise Exception('Invalid Index')
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return

        itr = self.head 
        count = 0
        while itr:
            if count == index:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                break
            itr = itr.next
            count += 1

if __name__ == '__main__':
    ll = DoublyLinkedList()
    ll.insert_at_start('C')
    ll.insert_at_start('B')
    ll.insert_at_start('A')
    ll.print_forward()
    ll.print_backward()
    ll.insert_at_end('D')
    ll.print_forward()    
    ll.new_Linked_List(['orange','banana','mango'])
    ll.print_forward()
    print(ll.get_length())
    ll.insert_at(2,'grapes')
    ll.print_forward()
    ll.remove_at(2)
    ll.print_forward()