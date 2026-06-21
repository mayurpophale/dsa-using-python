#rule no 1 always drew the diagram 
class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev = prev
        self.item = item
        self.next = next

class DLL:
    def __init__(self,start=None):
        self.start = start
    def is_empty(self):
        return self.start == None
    def insert_at_start(self,data):
        n = Node(None,data,self.start) # first element ke prev me none hota he,item me data ki value dal denge,next me pehele wale ka refrence dal denge
        if not self.is_empty(): # aagar list emoty nhi he to
            self.start.prev = n #start ke prev me n ka refrance 
        self.start = n # aagar list empty rahi to 
    def insert_at_last(self,data):
        temp = self.start #temp nav ka vARIBLE lenge or start se chalu karege
        if self.start != None: #aagar list empty nhi he to
            while temp.next != None: #last varible tk traverse
                temp = temp.next
        n = Node(temp,data,None) # node create karenge or prev me temp dalenge ,item me data or next me none
        if temp == None: #list empty he to
            self.start = n #start me n ka refrence
        else:
            temp.next = n #nhi to temp ke next maltab last element ke next me n ka refrence
    def search(self,data): # traverse karke data ko match karne nhi hoga to none ans rahega
        temp = self.start
        while temp is not None:
            if temp.item == data:     #same as SLL
                return temp
            temp = temp.next
        return None
    def insert_after(self,temp,data):
        if temp is not None: #List empty nhi he to
            n = Node(temp,data,temp.next)
            if temp.next is not None: #temp ke aage element nhi he to
                temp.next.prev=n 
            temp.next =n
    def print_list(self):
        temp = self.start #start se suru kel
        while temp is not None: # jab tab last nhi aata tab tak
            print(temp.item,end = " ") 
            temp=temp.next #increment
    
    def del_first(self):
        if self.start is not None: #list is not empty
            self.start=self.start.next #start me dusra ka refrance
            if self.start is not None: 
                self.start.prev = None
    def del_last(self):
        if self.start is None: #list empty
            pass
        elif self.start.next is None: #ek node he to
            self.start=None 
        else: #do aur usse jaad node he to
            temp = self.start #travese karenfge or last element ko delete karenge
            while temp.next is not None: #last element tk
                temp = temp.next #increment
            temp.prev.next = None #last second element ke next me none
    def del_item(self,data):
        if self.start is None:
            pass #list empty
        else:
            temp = self.start
            while temp is not None: #last element tk
                if temp.item == data:#value match ho gay to
                    if temp.next is not None: #temp ke bad node nhi he
                        temp.next.prev = temp.prev
                    if temp.prev is not None: #temp ke pahele node nhi he to
                        temp.prev.next = temp.next
                    else: #first node raha to
                        self.start=temp.next 
                    break
                temp=temp.next #increment
    def __iter__(self):
        return DLLIterator(self.start) #for making dll into the iterator

class DLLIterator:
    def __init__(self,start):
        self.current = start
    def __iter__(self):
        return self      #current is act as temp
    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current=self.current.next
        return data
    
mydlist = DLL()
mydlist.insert_at_start(3)
mydlist.insert_at_last(20)
mydlist.insert_at_start(30)
mydlist.insert_at_last(46)
mydlist.insert_after(mydlist.search(20),25)
mydlist.del_last()
mydlist.del_first()
mydlist.del_item(3)
for x in mydlist:
    print(x)