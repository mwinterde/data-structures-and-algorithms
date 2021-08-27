def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """

    if not ints:
        return None, None
    min_int = ints[0]
    max_int = ints[0]
    for current_int in ints[1:]:
        if current_int < min_int:
            min_int = current_int
        elif current_int > max_int:
            max_int = current_int
    
    return min_int, max_int

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

print ("Pass" if ((1, 1) == get_min_max([1, 1, 1])) else "Fail")
print ("Pass" if ((1, 1) == get_min_max([1])) else "Fail")
print ("Pass" if ((None, None) == get_min_max([])) else "Fail")