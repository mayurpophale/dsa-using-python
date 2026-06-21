#rule no 1 always draw the diagram
class Node:
    def __init__(self,item=None,next=None): #node create kara
        self.item = item
        self.next = next

class SLL:
    def __init__(self,start=None):
        self.start = start 
    def is_empty(self):
        return self.start == None #aagar start he none raha to list empty
    def insert_at_start(self,data):
        n = Node(data,self.start) #pahele ek node create karege usme data or uske next me start ka refrence dal denge
        self.start=n
    def insert_at_end(self,data):
        n = Node(data,None) # node create karene or usme data dal lenge
        if not self.is_empty():          #aag list empty nhi he to ye chalenga
            temp = self.start            #ek temp nam ka variable lenge for travarsing ke liye
            while temp.next is not None: #jab tak temp ke next me none maltab last node tak traverse karenge
                temp = temp.next
            temp.next = n # baad me usme temp ka refrence dal denge  
        else:
            self.start = n # aag list empty he to

    def search(self,data): 
        temp = self.start #temp nam ka varible declear karenge or usko start se suru karnge
        while temp is not None: # jab tak temp none nhi hota tab tk
            if temp.item == data: # aagar tempki value data se match karegi to temp return kardenge
                return temp
            temp = temp.next
        return None # aagar item mela nhi to none return karenge
    def insert_after(self,temp,data):
        if temp is not None: 
            n = Node(data,temp.next)
            temp.next = n
    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item,end=" ")
            temp = temp.next
    def delete_start(self):
        if self.start is not None: # aagar list empty nhi he to
            self.start = self.start.next 
    def delete_end(self):
        if self.start is None: #empty list
            pass 
        elif self.start.next is None: #aagar ek node raha to
            self.start = None
        else: # do or uuse jada rahe to
            temp = self.start
            while temp.next.next is not None:
                temp=temp.next
            temp.next=None
    def delete_item(self,data):
        if self.start is None: #empty list
            pass
        elif self.start.next is None: #aagar ek node raha to
            if self.start.item == data:
                self.start = None
        else:
            temp = self.start
            if temp.item == data:
                self.start = temp.next
            else:
                while temp.next is not None:
                    if temp.next.item == data:
                        temp.next = temp.next.next
                        break
                    temp = temp.next
    def __iter__(self):
        return SLLITERABTOR(self.start)

#for making sll into iterator
class SLLITERABTOR:
    def __init__(self,start):
        self.current = start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current=self.current.next
        return data


# mylist = SLL()
# mylist.insert_at_start(20)
# mylist.insert_at_start(30)
# mylist.insert_at_start(200)
# mylist.insert_at_start(300)
# mylist.insert_at_end(60)
# mylist.insert_after(mylist.search(30),40)
# mylist.insert_after()
# mylist.print_list()
# for i in mylist:
#     print(i)
# mylist.search(30)
# print(mylist.is_empty())