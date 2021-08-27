**Task0.py**

Time complexity: O(1)
* The code will always run in the same amount of time, regardless of the input
data

**Task1.py**

Time complexity: O(n)
* We loop through every row of the input data. In each iteration we do only
O(1) operations. Accordingly, the execution time will grow linearly with the
input data


**Task2.py**

Time complexity: O(n)
* We loop at maximum two times through every row of the input data. In each
iteration we do only O(1) operations. Accordingly, again the execution time
will grow linearly with the input data

**Task3.py**

Part A:
Time complexity: O(n log n)
* Actually, we loop through every row at maximum two times and do multiple
O(1) operations. So without sorting this would be a O(n) problem. But because
of the sorting it gets O(n log n).

Part B:
Time complexity: O(n)
* We loop through every row and do O(1) operations. So, this is a O(n) problem.


**Task4.py**

Time complexity: O(n log n)
* This time, we loop at maximum three times through every row. It would be a O
(n) problem without the sorting. But because of the sorting it gets O(n log n).
