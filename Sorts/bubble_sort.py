my_list = [2,5,7,10,1,5]

def bubble_sort(my_list):
    a = len(my_list)
    for b in range(a) :
        for x in range(0,a-b-1) :
            if my_list[x] >  my_list[x+1] :
                my_list[x], my_list[x+1] = my_list[x+1], my_list[x]
    return my_list
        


sorted_list = bubble_sort(my_list)
print(sorted_list)

