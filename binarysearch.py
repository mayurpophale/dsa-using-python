def binary_search(list,item):
    left =0
    right=len(list)-1

    while left <=right:
        mid = (left+right)//2

        if list[mid]==item:
            return list.index(item)
        elif list[mid] < item:
            left = mid+1
        else:
            right=right-1
    return None

l =[2,4,54,55,57,66,7777,67666,]
target = 4

print(binary_search(l,target))