def liner_search(my_list,target):
    for i in range(len(my_list)):
        if my_list[i] == target:
            return i
    return -1


my_list=[4,8,2,9]
target =int(input("adad :"))
result= liner_search(my_list,target)

if result != -1:
    print(f"{target} found at index: {result}")
else:
    print(f"{target} not found in the array")
