#Implenetation for deque using DLL
class Node:
    def __init__(self,item=None,prev=None,next=None):
        self.item = item
        self.prev = prev
        self.next = next

class Deque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.itemcount = 0
    
    def is_empty(self):
        return self.itemcount == 0
    
    def insert_front(self,data):
        n = Node(data,None,self.front)
        if self.is_empty():
            self.rear = n
        else:
            self.front.prev = n
        self.front =n
        self.itemcount +=1
    
    def insert_rear(self,data):
        n = Node(data,self.rear)
        if self.is_empty():
            self.front = n
        else:
            self.rear.next = n
        self.rear = n
        self.itemcount += 1
    def delete_front(self):
        if self.is_empty(): #empty list hoto
            raise Exception("empty list")
        if self.front == self.rear: #ek node hoto
            self.front = None
            self.rear = None
        else: #ek se jada node
            self.front = self.front.next #pehele me dusre ka refrance
            self.front.prev = None  #pehele ke prev se none delete
        self.itemcount -=1

    def delete_rear(self):
        if self.is_empty(): #empty list hoto
            raise Exception("empty list")
        if self.front == self.rear: #ek node hoto
            self.front = None
            self.rear = None
        else: #ek se jada node
            self.rear = self.rear.prev
            self.rear.next = None
        self.itemcount -=1
    
    def get_front(self):
        if self.is_empty(): #empty list hoto
            raise Exception("empty list")
        else:
            return self.front.item
    
    
    def get_rear(self):
        if self.is_empty(): #empty list hoto
            raise Exception("empty list")
        else:
            return self.rear.item
    
    def size(self):
        return self.itemcount

d = Deque()
d.insert_front(30)
d.insert_front(40)
d.insert_rear(50)
print(d.get_front())
print(d.get_rear())
print(d.size())