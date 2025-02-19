def print_list(num_list):
    print(num_list)

def merge_sort(original_list):
    if len(original_list) <= 1:
        return

    mid = len(original_list) // 2
    
    lefthalf = original_list[:mid]
    righthalf = original_list[mid:]

    merge_sort(lefthalf)
    print_list(lefthalf)
    
    merge_sort(righthalf)
    print_list(righthalf)

    i = 0 # Index for the left half list
    j = 0 # Index for the right half list
    k = 0 # Index for the original list

    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] < righthalf[j]:
            original_list[k] = lefthalf[i]
        
            i = i + 1
        else:
            original_list[k] = righthalf[j]
            j = j + 1
        k=k+1

    while i < len(lefthalf):
        original_list[k] = lefthalf[i]
        
        i = i + 1
        k = k + 1

    while j < len(righthalf):
        original_list[k] = righthalf[j]

        j = j + 1
        k = k + 1

num_list = [54, 26, 93, 17, 77, 31, 44, 55, 20, 13, 2, 100, 66]

merge_sort(num_list)

print(num_list)