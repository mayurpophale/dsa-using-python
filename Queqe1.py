#implementation of queqe using list
class Queqe:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def enqueqe(self,data):
        self.items.append(data)
    
    def dequeqe(self):
        if not self.is_empty():
            self.items.pop(0) #front wale se nikala
        else:
            raise Exception("Underflow")
        
    def get_front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise Exception("Underflow")
        
    def get_rear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise Exception("Overflow")
    
    def size(self):
        return len(self.items)
    

q = Queqe()
q.enqueqe(20)
q.enqueqe(30)
q.enqueqe(40)
q.enqueqe(50)
q.enqueqe(70)
# print(q.dequeqe(),
# q.get_front(),
# q.get_rear(),
# q.is_empty(),
# q.size())