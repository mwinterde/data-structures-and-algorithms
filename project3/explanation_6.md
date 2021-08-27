We can traverse through the list of integers once, if we keep track of the minimum and maximum
in each iteration. Therefore, the time complexity of this solution becomes O(n) and the 
space complexity O(1). I choose to implement the variables for the current minimum and maximum
value, as therefore we can avoid sorting of the input array. Sorting would have lead to worse
time complexity.