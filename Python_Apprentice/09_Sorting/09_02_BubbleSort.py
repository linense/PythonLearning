def print_list(num_list):
    print(num_list)

def bubble_sort(original_list):
    
    length = len(original_list)

    for i in range(length - 1, 0, -1):
        
        for index in range(i):
            
            if original_list[index] > original_list[index + 1]:
                
                original_list[index + 1], original_list[index] = original_list[index], original_list[index + 1]

        print('Unsorted till index: ', i - 1)
        print_list(original_list)
    
student_marks = [88, 99, 34, 32, 43, 25, 29, 45, 49, 37]
bubble_sort(student_marks)

flowers_list = ['Sunflower', 'Freesia', 'Daffodil', 'Anemone', 'Asiatic Lily', 'Jasmine']
bubble_sort(flowers_list)