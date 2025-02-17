def print_list(num_list):
    print(num_list)

def insertion_sort(original_list):
    
    length = len(original_list)
    
    for i in range(0, length - 1):
        
        for j in range(i + 1, 0, -1):       
            if original_list[j] < original_list[j - 1]:
                
                original_list[j], original_list[j - 1] = \
                    original_list[j - 1], original_list[j]

        print('Sorted till index: ', i)
        print_list(original_list)

def insertion_sort2(original_list):
    
    length = len(original_list)
    
    for i in range(0, length - 1):
        
        for j in range(i + 1, 0, -1):       
            if original_list[j] < original_list[j - 1]:
                
                original_list[j], original_list[j - 1] = \
                    original_list[j - 1], original_list[j]
            else:
                break

        print('Sorted till index: ', i)
        print_list(original_list)

a = [10, 5, 7, 2, 8, 3, 9, 6, 1, 4]

insertion_sort(a)