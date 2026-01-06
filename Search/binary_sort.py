def binary_search(my_list,target):
    left = 0
    right = len(my_list)-1

    while left <= right :
        mid = (left+right)//2
        if target == my_list[mid]:
            return mid
        if target > mid:
            left = mid +1
        else :
            right = mid -1
    return -1

my_list=[1,2,7,9]
target = 7
result = binary_search(my_list,target)
print(f"adad :{target} hast dar index :{result}")
