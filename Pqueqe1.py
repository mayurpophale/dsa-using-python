#Priority queqe using list
#tihs is look like [(20,1),(40,3),(60,4)] list to tuples where 1st index in data and 2nd is its priorityy
class PriorityQueqe:
    def __init__(self):
        self.items = []
    
    def push(self,data,priotityy):
        index = 0
        while index < len(self.items) and self.items[index][1] <= priotityy:
            index += 1
        self.items.insert(index,(data,priotityy))

    def is_empty(self):
        return len(self.items) == 0
    
    #poping the highest proiority element
    def pop(self):
        if self.is_empty():
            raise Exception("Emptyyyyyyyyyy")
        else:
            return self.items.pop(0)[0]
    
    def size(self):
        return len(self.items)
    
p = PriorityQueqe()
p.push(20,3)
p.push(40,1)
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