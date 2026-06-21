from SLL import *
class Stack(SLL):
    def __init__(self):
        super().__init__() #parent ke init ko include kar diyaa
        self.itemcount = 0
    def is_empty(self):
        return super().is_empty()
    
    def push(self,data):
        self.insert_at_start(data)
        self.itemcount += 1
    
    def pop(self):
        if not self.is_empty():
            self.delete_start()
        self.itemcount -= 1
    
    def peak(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise IndexError("Underflow")
    def size(self):
        return self.itemcount
    
s = Stack()
s.push(30)
s.push(40)
s.push(200)
s.pop()
print(s.peak())
print(s.size())