def insertion_sort(list):
    for i in range(1,len(list)):
        temp = list[i]

        j = i-1
        while j>=0 and temp < list[j]:
            list[j+1] = list[j]
            j -=1

        list[j+1] = temp

l= [2,22,3,222222222,34,55]
insertion_sort(l)
print(l)