#Implementation of queqe using linkedlist
class Node:
    def __init__(self,item=None,next=None):
        self.item = item
        self.next = next
        
class Queqe:
    def __init__(self):
        self.front = None
        self.rear = None
        self.itemcount = 0
    
    def is_empty(self):
        return self.front== None or self.rear == None or self.itemcount == 0
    
    def enqueqe(self,data):
        #aare list empty nhi he to sir rear me changes honge or aagar list empty rhi to front or rear dono me changes karne padenge
        n = Node(data)
        if self.is_empty():
            self.front = n
        else:
            self.rear.next = n
        self.rear = n
        self.itemcount +=1

    def dequeqe(self):
        if self.is_empty(): #empty 
            raise Exception("Empty queqe")
        elif self.front == self.rear: #only one node
            self.front = None
            self.rear = None
        else: #more than one queqe
            self.front = self.front.next
        self.itemcount -=1
    
    def get_front(self):
        if self.is_empty():
            raise Exception("No data in queqe")
        else:
            return self.front.item
    
    def get_rear(self):
        if self.is_empty():
            raise Exception("No data in queqe")
        else:
            return self.rear.item
        
    def size(self):
        return self.itemcount
    
q = Queqe()
q.enqueqe(30)
q.enqueqe(40)
q.enqueqe(70)
q.enqueqe(90)
q.enqueqe(110)
q.dequeqe()
print(q.get_front())
print(q.get_rear())

print(q.is_empty())

print(q.size())