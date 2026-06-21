def selection_sort(list):
    n = len(list)
    for i in range(n-1):
        min_index = i
        for j in range(i+1,n):
            if list[j] < list[min_index]:
                min_index = j
        list[i],list[min_index] = list[min_index],list[i]

l = [12,32,22,1,4,55,7,99]
selection_sort(l)
print(l)