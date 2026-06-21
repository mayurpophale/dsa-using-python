#Priority queqe using SLL
class Node:
    def __init__(self,item=None,priority=None,next=None):
        self.item = item
        self.priority = priority
        self.next = next

class PriorityQueqe:
    def __init__(self):
        self.start = None
        self.itemcount = 0

    def is_empty(self):
        return self.itemcount == 0
    
    def push(self,data,priority):
        n =Node(data,priority)
        if not self.start or priority < self.start.priority:
            n.next = self.start
            self.start = n

        else:
            temp = self.start
            while temp.next and temp.next.priority <= priority:
                temp = temp.next
            n.next = temp.next
            temp.next = n
        self.itemcount +=1

    def pop(self):
        if self.is_empty():
            raise IndexError("balalalalaaaaaa")
        else:
            data= self.start.item
            self.start = self.start.next
            self.itemcount -=1
            return data

    def size(self):
        return self.itemcount
p =PriorityQueqe()
p.push(20,3)
p.push(40,1)
p.push(400,11)
p.push(56,7)
print(p.pop())
print(p.size())
print()
print(p.pop())
print(p.size())
print()
print(p.pop())
print(p.size())
print()    
    

        