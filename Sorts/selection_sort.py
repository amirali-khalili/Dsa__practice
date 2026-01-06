def selection_sort(my_list):
    k = len(my_list)
    for i in range(k):
        min_ins = i
        for j in range(i+1,k):
            if my_list[min_ins] > my_list[j]:
                min_ins = j 
        my_list[i], my_list[min_ins] = my_list[min_ins] , my_list[i]
    return my_list

my_list=[5,3,8,1]
print(selection_sort(my_list))