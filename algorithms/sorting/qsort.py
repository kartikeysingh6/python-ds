"""
High level(English) explanation:
Quicksort algorithm is that if we can efficiently partition a list, 
then we can efficiently sort it. Partitioning a list means that 
we pick a pivot item in the list, and then modify the list 
to move all items larger than the pivot to the right and all 
smaller items to the left.

Once the pivot is done, we can do the same operation to the 
left and right sections of the list recursively until the list is sorted.

Time complexity:
Best Time complexity: Omega(n log n).
Average Time complexity: Theta(n log n).
Worst Time complexity: O(n^2)   -Can be avoided easily by Randomized QuickSort

Space complexity:
Average Space complexity: Theta(log n) = It's so small its approximately O(1)
Worst Space complexity: O(n)    -Can be avoided easily by Randomized QuickSort

Characterstics:
1. Divide and Conquer approach.
2. Recursion based.
3. Unstable (If elements are same their relative position might change)
4. Inplace (Constant Space complexity)
"""


def qsort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr.pop()
    """Un-comment the below code to impletemt randomized QuickSot so that
    pivot is randomly selected and has high probability of time complexity of
    O(nlogn)
    
    NOTE: Make sure to import random library for random function to work.
    """
    #pivot = arr.pop(random.randint(0,len(arr)))
    greater, lesser = [], []
    for item in arr:
        if item > pivot:
            greater.append(item)
        else:
            lesser.append(item)
    return qsort(lesser) + [pivot] + qsort(greater)
