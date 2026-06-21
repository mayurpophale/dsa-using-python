def merge_sort(list):
    if len(list) > 1:
        mid = len(list)//2
        leftlist = list[:mid]
        rightlist = list[mid:]

        merge_sort(leftlist)
        merge_sort(rightlist)
        i=j=k=0
        while i < len(leftlist) and j<len(rightlist):
            if leftlist[i] < rightlist[j]:
                list[k] =leftlist[i]
                i+=1
            else:
                list[k] = rightlist[j]
                j+=1
            k+=1
        
        while i < len(leftlist):
            list[k] = leftlist[i]
            i+=1
            k+=1

        while j < len(rightlist):
            list[k] = rightlist[j]
            j+=1
            k+=1

l = [ 33,4,55,34,2,53,535,646,673,55,43,1,3,455,6666,773,5 ]
merge_sort(l)
print(l)