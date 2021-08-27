I choose to implement to pointers that keep track of the next index for moving a `0`
or `2`. Therefore, we can sort the array in a single traversal with O(n) time complexity
and O(1) space complexity. The strategy works only for problems where we have to sort
three or less numbers. With more than three numbers, it wouldn't be possible to implement
the pointers effectively in a 2D array.