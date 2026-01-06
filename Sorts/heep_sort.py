def heap_sort(my_list):
    n = len(my_list)

    for j in range(n//2-1,-1,-1):
        heapfy(my_list,n,j)

    for k in range(n-1,0,-1):
        my_list[0],my_list[k]=my_list[k],my_list[0]
        heapfy(my_list,k,0)

    return my_list


def heapfy(my_list,n,i):
    largest = i
    left = i*2 +1
    right = i*2 +2

    if left <n and my_list[largest]<my_list[left]:
        largest = left
    if right <n and my_list[largest] < my_list[right]:
        largest = right
    
    if largest != i :
        my_list[i],my_list[largest] = my_list[largest],my_list[i]
        heapfy(my_list,n,largest)


my_list = [4,3,8,0,2]
print(heap_sort(my_list))