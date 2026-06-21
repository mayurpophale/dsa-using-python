def bubble_sort(list):
    for r in range(1,len(list)): #no of rounds
        for i in range(len(list)-r): #har round ke baad ke value sort hogi or ek comp kam hoga
            if list[i] > list[i+1]:
                list[i],list[i+1] = list[i+1],list[i]
    return list

#modify bubble sort
def modify_bubble_sort(list):
    flag = False
    for r in range(1,len(list)): #no of rounds
        flag = False
        for i in range(len(list)-r): #har round ke baad ke value sort hogi or ek comp kam hoga
            if list[i] > list[i+1]:
                list[i],list[i+1] = list[i+1],list[i]
                flag = True
        if not flag:
            break #agar list k round me sort hogi to aage comperision nhi hogaa
            

l = [20,30,4,3,2,1]
l1 = [20,4,5,6,7,77777,4]
print(bubble_sort(l))
modify_bubble_sort(l1)
print(l1)