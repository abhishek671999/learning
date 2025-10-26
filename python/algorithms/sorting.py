import math

def bubble_sort(array):
    for j in range(len(array)):
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]: 
                temp = array[i + 1]
                array[i + 1] = array[i]
                array[i] = temp
    return array


def selection_sort(array):
    for i in range(len(array)):
        min = i 
        temp = array[min]
        for j in range(len(array) - i):
            if array[min] > array[i + j]:
                min = i + j
        array[i] = array[min]
        array[min] = temp    
    return array
        
def splice(array, start_index, length=0, new_elements=[]):
    removed_elements = array[start_index: start_index+length]
    array[start_index: start_index+length] = new_elements
    return removed_elements

# def insertion_sort(array):
# Copied from course | Not working unfortunately
#     for i in range(len(array)):
#         if array[i] < array[0]:
#             array.insert(0, splice(array, i, 1)[0])
#         else:
#             for j in range(1, i):
#                 if array[i] > array[j-1] and array[i] < array[j]:
#                     splice(array, j, 0, splice(array, i, 1))
#     return array

def insertion_sort(array):
    for i in range(len(array)):
        if i == 0:
            pass
        else:
            for j in range(i):
                if array[i] < array[j]:
                    temp_ele = array[i]
                    spliced_ele = splice(array, j, i - j)
                    splice(array, j, 1, [temp_ele] + spliced_ele)
    return array

def merge(array1, array2):
    merged_array = []
    array1_pointer = 0
    array2_pointer = 0
    while array1_pointer < len(array1) or array2_pointer < len(array2):
        # can also use slice at the end instead of these additional here
        if array1_pointer == len(array1):
            merged_array.append(array2[array2_pointer])
            array2_pointer += 1
        elif array2_pointer == len(array2):
            merged_array.append(array1[array1_pointer])
            array1_pointer += 1
        elif array1[array1_pointer] < array2[array2_pointer]:
            merged_array.append(array1[array1_pointer])
            array1_pointer += 1
        else:
            merged_array.append(array2[array2_pointer])
            array2_pointer += 1
    return merged_array

def merge_sort(array):
    if len(array) == 1:
        return array
    length = len(array)
    half_length = math.floor(length/2)
    left = array[0: half_length]
    right = array[half_length: ]
    
    return merge(
            merge_sort(left),
            merge_sort(right)
        )

if __name__ == '__main__':
    array = [9, 1, 3, 2, 4, 2, 0, 73, 21, 92, 11]
    # array = [1, 3, 2, 4, 2, 0, 73, 21, 92, 11]
    print(
        'original ', array,
        'sorted ', insertion_sort(array.copy()), '\n',
        )
    print(
        'original ', array,
        'sorted ', selection_sort(array.copy()), '\n',
        )
    print(
        'original ', array,
        'sorted ', merge_sort(array.copy()), '\n',
        )