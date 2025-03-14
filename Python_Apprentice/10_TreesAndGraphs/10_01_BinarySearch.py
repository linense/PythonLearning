def binary_search(sorted_list, key):
    min_index = 0
    max_index = len(sorted_list) - 1
    
    while(min_index <= max_index):
        mid = (min_index + max_index) // 2

        if sorted_list[mid] == key:
            return mid
        elif sorted_list[mid] < key:
            min_index = mid + 1
        else:
            max_index = mid - 1
            
    return -1

num_list = [25, 29, 32, 34, 37, 43, 45, 49, 55, 66, 78, 89, 99]
print(binary_search(num_list, 45))
print(binary_search(num_list, 32))
print(binary_search(num_list, 78))
print(binary_search(num_list, 88))