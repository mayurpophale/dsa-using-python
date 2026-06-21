#Diagram is imp
#In this type linked list look like 
# last --> lastnode --> --            --> firstnode             firstnode ka next me last ka refrance 
#           ^--------------------------------^
class Node:
    def __init__(self,item=None,next=None):
        self.item = item
        self.next = next

class CLL:
    def __init__(self,last=None):
        self.last = last
    def is_empty(self): 
        return self.last == None #last elemet me kuch nhi hoga to empty 
    def insert_at_start(self,data):
        n=Node(data)
        if self.is_empty(): # agr list empty he to
            n.next = n #new node ke next me kudka referance dal denge
            self.last = n #last node me new node ka refrance
        else: #aagr empty nhi he to
            n.next = self.last.next #new ke next me last ke next ka refrance(pehela element)
            self.last.next = n #last ke next me n ka refrance

    def insert_at_last(self,data):
        n= Node(data)
        if self.is_empty(): # agr list empty he to
            n.next = n #new node ke next me kudka referance dal denge
            self.last = n #last node me new node ka refrance
        else:
            n.next = self.last.next #new ke next me last ke next ka refrance(pehela element)
            self.last.next = n #last ke next me n ka refrance
            self.last = n #last node me new node ka refrance
    def search(self,data):
        if self.is_empty():
            return None
        #aagar list empty nhi to ye ocde chalega
        temp = self.last.next # temp me pehelka ka refrance
        while temp != self.last: #last ke element ko chod ke sab ko check karleya
            if temp.item== data: #checking
                return temp 
            temp = temp.next # increamet
        if temp.item == data: #last element ke liye
            return temp
        return None #aagar kuch nhi mila to none
    def insert_after(self,temp,data):
        if temp is not None: #aagr temp me none nhi he to matlab list empty na ho to
            n = Node(data,temp.next)
            temp.next =n
            if temp == self.last: # temp last element he to
                self.last = n 
    
    def print_list(self):
        if not self.is_empty(): #aagar list empty nhi he to
            temp=self.last.next #first element 
            while temp != self.last: #loop first se lasst tk chalega pr last ke element ko access nhi kar payega
                print(temp.item,end=" ")
                temp = temp.next
            print(temp.item) #last element ko print karega
    
    def delete_first(self):
        if not self.is_empty(): #aagar list empty nhi he to
            if self.last.next == self.last: #ek hee node ho to
                self.last = None # pehele me none dal denge
            else:
                self.last.next = self.last.next.next #pehle me durse ka refrance

    def delete_last(self):
        if not self.is_empty(): #aagar list empty nhi he to
            if self.last.next == self.last: #ek hee node ho to
                self.last = None # pehele me none dal denge
            else: #kam se kam do node ho to
                temp = self.last.next #traversing
                #last second node se last ka refrance nekal denge
                while temp.next != self.last:
                    temp = temp.next #increemnet
                temp.next = self.last.next #last me first ka refrance
                self.last = temp #last me temp ka refrnce
    def delete_item(self,data):
        if not self.is_empty(): #aagar list empty nhi he to
            if self.last.next == self.last: #ek hee node ho to
                if self.last.item == data: # aagar wo ek element ke value data ke equal ho to 
                    self.last = None 
            else: #aagar ek se jada node ho to
                if self.last.next.item == data:#aagar pehela he node delete karna he to
                    self.delete_first()
                else:
                    temp = self.last.next #first node
                    while temp != self.last:#last node ko chod ke sab
                        if temp.next==self.last:#temp ke next me last ke value
                            if self.last.item == data:#aagar value equal ho to
                                self.delete_last() 
                                break
                        if temp.next.item == data: #aagar element mel gaya to
                            temp.next = temp.next.next #temp ke next me uske next ke value dal denge
                            break
                        temp = temp.next #increment

cll = CLL()
cll.insert_at_last(30)
cll.insert_at_start(20)
cll.insert_at_start(300)
cll.insert_after(cll.search(30),31)
cll.delete_item(300)
cll.print_list()
                             
