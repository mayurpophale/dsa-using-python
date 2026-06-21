#Implementation of stack using linked list 
from SLL import * #importing all things of sll

class Stack:
    def __init__(self):
        self.mylist = SLL()
        self.itemcount = 0

    def is_empty(self):
        return self.mylist.is_empty()
    
    def push(self,data):
        self.mylist.insert_at_start(data)
        self.itemcount += 1
    
    def pop(self):
        if not self.is_empty():
            self.mylist.delete_start()
            self.itemcount -=1

    def peek(self):
        if not self.is_empty():
            return self.mylist.start.item
        
    def size(self):
        return self.itemcount
    
s = Stack()
s.push(10)
s.push(20)
s.push(10000)
s.push(100)
s.push(1011)
s.pop()
print(s.peek())