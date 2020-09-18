''' 
    First sort the array. It would be even better if the array is already sorted. 
    Then take two variables and initialize them with the starting two indexes of the
    array. Traverse the array. Check the difference between `j` and `i`th index
    (assuming j is 1st index and i is 0th index). If it is k then simply increase the
    counter. If the difference is less than k, we need to increase the difference, so 
    increment j. Else if the difference is greater than k, we need to decrease the 
    difference, so increment i.

    An alternate solution would be to use a hashmap. If the array is not sorted it would 
    take the time and space complexity O(n) while this solution takes time complexity 
    O(nlogn) because of sorting. 
'''

import math
import os
import random
import re
import sys

# Complete the pairs function below.
def pairs(k, arr):
    arr.sort()
    count = 0
    i = 0
    j = 1
    while i<len(arr) and j<len(arr):
        if  i<j and arr[j] - arr[i] == k:
            count += 1
            i += 1
            j += 1
        elif arr[j] - arr[i] < k:
            j += 1
        else:
            i += 1
    return count 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()