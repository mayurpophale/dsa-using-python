def linear_search(list,item):
    for i in list:
        if item == i:
            return list.index(i)
        return None
    
l = [2,4,55,66,75,744,664,3]
a= linear_search(l,5)
print(a)