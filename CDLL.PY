#rule no 1 always drew the diagram 
class Node:
    def __init__(self,item=None,prev=None,next=None):
        self.item = item
        self.prev = prev
        self.next = next

class CDLL:
    def __init__(self,start=None):
        self.start = start
    def is_empty(self):
        return self.start == None
    def insert_at_first(self,data):
        n = Node(data)
        if self.is_empty(): #aagae list empty he to
            n.next = n #next ani prev me khud ka he refrance dal denge
            n.prev = n
        else:
            n.next = self.start #pehele do line ne node creaction complete hogya and next do ani me usko linkedlist me add kardiyaa
            n.prev = self.start.prev
            self.start.prev.next = n #last element kee next me n ka refrance
            self.start.prev = n #first node ke prev me n ka refrance
        self.start = n 
    
    def insert_at_last(self,data):
        n = Node(data)
        if self.is_empty(): #aagae list empty he to
            n.next = n #next ani prev me khud ka he refrance dal denge
            n.prev = n
            self.start = n
        else:
            n.next = self.start
            n.prev = self.start.prev
            n.prev.next = n
            self.start.prev = n

    def search(self,data): # traverse karke data ko match karne nhi hoga to none ans rahega
        temp = self.start
        if temp==None: #empty list
            return None
        if temp.item == data: #data found
            return temp
        else:
            temp = temp.next
        while temp is not None:
            if temp.item == data:     #same as SLL
                return temp
            temp = temp.next
        return None
    def insert_after(self,temp,data):
        if temp is not None: #list is not empty
            n = Node(data)
            n.next = temp.next
            n.prev = temp
            temp.next.prev = n
            temp.next = n

    def print_list(self):
        temp = self.start #start se suru kel
        if temp is not None: #list is not empty
            print(temp.item,end=" ") 
            temp = temp.next #increment

            while temp is not self.start: # jab tab ek bar fir se start tk nhi aata tab tk
                print(temp.item,end = " ") 
                temp=temp.next #increment
    
    def delete_first(self):
        if self.start is not None:#empty na ho to
            if self.start.next == self.start:#ek node ho to
                self.start = None
            else:#ek se jada node ho to
                self.start.prev.next = self.start.next #last ke next me second ka refrance
                self.start.next.prev = self.start.prev #second ke prev ko last ka refrance
                self.start= self.start.next #start me second wala ka refrance
    def delete_last(self):
        if self.start is not None:#empty na ho to
            if self.start.next == self.start:#ek node ho to
                self.start = None
            else:
                self.start.prev.prev.next = self.start #second last ke next me start ka refrance
                self.start.prev = self.start.prev.prev #pehele ke prev me second last ke prev ka refrance
    def delete_item(self,data):
        if self.start is not None:#empty na ho to
            temp = self.start
            if temp.item == data:
                self.delete_first()
            else:
                temp = temp.next
                while temp is not self.start:#fir ke start tk na aaye tb tk
                    if temp.item == data:
                        temp.next.prev = temp.prev
                        temp.prev.next = temp.next
                    temp = temp.next #increment
    
mylist = CDLL()
mylist.insert_at_first(30)
mylist.insert_at_first(40)
mylist.insert_at_last(140)
mylist.insert_at_first(5)
mylist.insert_after(mylist.search(140),50)
mylist.delete_item(5)
mylist.print_list() # 40 -> 30 -> 140 -> 50


