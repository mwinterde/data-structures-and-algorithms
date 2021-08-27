My approach follows two steps:

First, we are building a min heap from the input list, which results in O(n log n) time complexity.
Why? Because each `heapify` call costs O(log n) and we make in total O(n) of these calls.

Second, we are constructing the output numbers by removing all elements from the heap one by one.
With the same logic, this results in O(n log n) time complexity.

So in total my approach is O(n log n). 

The space complexity of my solution is O(n) since we construct a heap in the first step,
which works on a complete copy of the input array.