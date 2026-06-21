#implentation of stack using list
class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def push(self,data):
        self.items.append(data)
        
    def pop(self):
        if not self.is_empty(): #not empty list
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")
    
    def peek(self):
        if not self.is_empty(): #not empty list
            return self.items[-1]
        else:
            return IndexError("Stack is empty")
    def size(self):
        return len(self.items)

mystack = Stack()
mystack.push(20)
mystack.push(40)
mystack.push(50)
mystack.push(70)
mystack.pop()
print(mystack.is_empty())
print(mystack.peek())
# print(mystack.pop())


