def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """

    if not input_list:
        return -1
   
    pivot_index = _find_pivot(input_list)
    unrotated_array = input_list[pivot_index:]+input_list[:pivot_index]
    lower_index = 0
    upper_index = len(unrotated_array) - 1
    
    while lower_index <= upper_index:
        middle_index = lower_index + (upper_index-lower_index) // 2
        if unrotated_array[middle_index] == number:
            L = len(input_list)
            if middle_index <= (L - pivot_index):
                return pivot_index + middle_index
            else:
                return middle_index - (L - pivot_index)
        elif unrotated_array[middle_index] < number:
            lower_index = middle_index + 1
        else:
            upper_index = middle_index - 1
    
    return -1


def _find_pivot(array):

    if array[-1] > array[0]:
        return 0

    lower_index = 0
    upper_index = len(array)-1

    while lower_index < upper_index:
        middle_index = lower_index + (upper_index - lower_index) // 2
        if array[middle_index] < array[0]:
            upper_index = middle_index
        else:
            lower_index = middle_index + 1
        
    return upper_index


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")
        print(linear_search(input_list, number))
        print(rotated_array_search(input_list, number))


test_function([[1, 2, 3, 4, 6, 7, 8, 9, 10], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

test_function([[1, 2, 3, 4, 5], 6])
test_function([[], -1])