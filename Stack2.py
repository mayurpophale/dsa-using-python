#Implementation of stack using inheriting list class
#jo bhi stack ka object he wo list ka bhi object hoga
class Stack(list): # inheriting the list class
    def is_empty(self):
        return len(self) == 0
    
    def push(self,data):
        self.append(data)
        
    def pop(self):
        if not self.is_empty(): #not empty list
            return super().pop() #due to method overloading
        else:
            raise IndexError("Stack is empty")
    
    def peek(self):
        if not self.is_empty(): #not empty list
            return self[-1]
        else:
            return IndexError("Stack is empty")
    def size(self):
        return len(self)
    
    #restrict that properties of list that not follow the rules of stack llike insert at any index
    def insert(self, index, data):
        raise AttributeError("No such method in stack")

mystack = Stack()
mystack.push(20)
mystack.push(40)
# mystack.insert(3,50)

print(mystack.is_empty())
print(mystack.peek())