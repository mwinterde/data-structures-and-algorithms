We are structuring the task into two subproblems here, both of which have O(log n) time complexity:
1. Finding the index of the pivot and using it to create an unrotated copy of the sorted input array. 
2. Searching the input number in the unrotated array and translate its index back to the actual input. 

For both problems, we reduce the solution space by half in each iteration, therefore both algorithms have O(log n) time complexity. Since they take place one after the other, the overall time complexity is still O(log n). 

The space complexity of the problem is O(n) since we create an unrotated copy of the input array in step 1.