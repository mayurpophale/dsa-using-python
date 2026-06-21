class Node:
    def __init__(self,item=None,prev=None,next=None):
        self.item = item
        self.prev = prev
        self.next = next

class Deque:
    def __init__(self):
        self.items= []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def insert_front(self,data):
        self.items.insert(0,data)
    
    def insert_rear(self,data):
        self.items.append(data)
    
    def delete_front(self):
        if self.is_empty():
            raise Exception("Empty list")
        else:
            self.items.pop(0)
    def delete_rear(self):
        if self.is_empty():
            raise Exception("Empty list")
        else:
            self.items.pop()
        
    def get_front(self):
        if self.is_empty():
            raise Exception("Empty list")
        else:
            return self.items[0]
   
    def get_rear(self):
        if self.is_empty():
            raise Exception("Empty list")
        else:
            return self.items[-1]
    
    def size(self):
        return len(self.items)

q = Deque()
q.insert_rear(20)
q.insert_rear(40)
q.insert_front(25)
print(q.get_rear())
print(q.get_front())
print(q.is_empty())
        

        