def quick_sort(my_list):
    if len(my_list) <= 1 :
        return my_list
    
    pivot = my_list[0]
    left = []
    right = []

    for i in my_list[1:]:
        if i <= pivot :
            left.append(i)
        else :
            right.append(i)

    return quick_sort(left) + [pivot] + quick_sort(right)


my_list = [2,8,1,5]
print(quick_sort(my_list))