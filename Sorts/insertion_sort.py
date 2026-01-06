def insertion_sort(my_list):
    for i in range(1,len(my_list)):
        key = my_list[i]
        j = i - 1

        while j >=0 and my_list[j] > key :
            my_list[j +1] = my_list[j]
            j -= 1
        my_list [j+1] = key
    return my_list


my_list = [10,2,210,0,1]
print(insertion_sort(my_list))