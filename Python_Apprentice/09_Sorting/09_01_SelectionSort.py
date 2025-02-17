def print_list(num_list):
    print(num_list)

def selection_sort(original_list):
    
    length = len(original_list)
    
    for i in range(length):

        min_value_index = i
        print("Debug. ", i+1, ". iteration of the outer for-loop.")
        for j in range(i + 1, length):
            print("Debug. min_value_index=", min_value_index)
            print("Debug. original_list[min_value_index]=", original_list[min_value_index])
            print("Debug. original_list[j]=", original_list[j])
            if original_list[min_value_index] > original_list[j]:
                print("Debug. Entered the if-clause, min_value_index is set to j.")
                min_value_index = j
        
        original_list[i], original_list[min_value_index] = original_list[min_value_index], original_list[i]

        print('Sorted till index: ', i)
        print_list(original_list)

    print('Sorted list: ')
    print_list(original_list)

num_list = [10, 11, 5, 7, 2, 8, 3, 9, 6, 1, 4]

#print(num_list)
#print(len(num_list))
selection_sort(num_list)
