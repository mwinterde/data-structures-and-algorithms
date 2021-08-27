I choose to search the solution space with an approach that is similar to binary search, meaning that we split the solution space by half in each iteration. Therefore, the time complexity of the problem becomes O(log n). Moreover, we only need to keep track of the integers `lower`, `middle` and `upper` which leads to O(1) space complexity.