def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    
    # Create min heap from input list
    heap = Heap()
    for element in input_list:
        heap.insert(element)
    
    # Derive numbers for maximum sum
    number1, number2 = 0, 0
    i = 0
    while not heap.is_empty():
        number1 += _zeroifnull(heap.remove()) * 10**i
        number2 += _zeroifnull(heap.remove()) * 10**i
        i += 1
    
    return number1, number2

def _zeroifnull(value):
    return value if value else 0


class Heap:
    def __init__(self, initial_size=10):
        self.cbt = [None for _ in range(initial_size)]  
        self.next_index = 0  

    def insert(self, data):
        self.cbt[self.next_index] = data
        self._up_heapify()
        self.next_index += 1
        if self.next_index >= len(self.cbt):
            temp = self.cbt
            self.cbt = [None for _ in range(2 * len(self.cbt))]
            for index in range(self.next_index):
                self.cbt[index] = temp[index]
    
    def remove(self):
        if self.size() == 0:
            return None
        self.next_index -= 1
        to_remove = self.cbt[0]
        last_element = self.cbt[self.next_index]
        self.cbt[0] = last_element
        self.cbt[self.next_index] = to_remove
        self._down_heapify()
        return to_remove

    def size(self):
        return self.next_index 
    
    def is_empty(self):
        return self.size() == 0
    
    def _up_heapify(self):
        child_index = self.next_index
        while child_index >= 1:
            parent_index = (child_index - 1) // 2
            parent_element = self.cbt[parent_index]
            child_element = self.cbt[child_index]
            if parent_element > child_element:
                self.cbt[parent_index] = child_element
                self.cbt[child_index] = parent_element
                child_index = parent_index
            else:
                break
    
    def _down_heapify(self):
        parent_index = 0
        while parent_index < self.next_index:
            left_child_index = 2 * parent_index + 1
            right_child_index = 2 * parent_index + 2
            parent = self.cbt[parent_index]
            left_child = None
            right_child = None
            min_element = parent
            # check if left child exists
            if left_child_index < self.next_index:
                left_child = self.cbt[left_child_index]
            # check if right child exists
            if right_child_index < self.next_index:
                right_child = self.cbt[right_child_index]
            # compare with left child
            if left_child is not None:
                min_element = min(parent, left_child)
            # compare with right child
            if right_child is not None:
                min_element = min(right_child, min_element)
            # check if parent is rightly placed
            if min_element == parent:
                return
            if min_element == left_child:
                self.cbt[left_child_index] = parent
                self.cbt[parent_index] = min_element
                parent = left_child_index
            elif min_element == right_child:
                self.cbt[right_child_index] = parent
                self.cbt[parent_index] = min_element
                parent = right_child_index


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print(output)
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])

test_function([[9, 3, 2, 4], [93, 42]])
test_function([[1, 4, 6, 7, 8, 2], [862, 741]])
test_function([[8, 9, 8], [98, 8]])
test_function([[9], [9]])
test_function([[], []])

