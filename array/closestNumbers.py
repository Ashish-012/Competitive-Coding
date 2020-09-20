'''
    Sort the array and just check all the neighbouring ekements maintaining the minimum
    absolute difference. Then iterate through the array again and append all the elements
    with the minimum difference (that we found in first time scanning).
'''

import math
import os
import random
import re
import sys

# Complete the closestNumbers function below.
def closestNumbers(arr):
    
    low = 99999999
    ans = []
    arr.sort()
    for i in range(len(arr)-1):
        j = i+1
        m = abs(arr[i]-arr[j])
        if m < low:
            low = m
    for i in range(len(arr)-1):
        j = i+1
        if abs(arr[j]-arr[i]) == low :
            ans.append(arr[i])
            ans.append(arr[j])
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()