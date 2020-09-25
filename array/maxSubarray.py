'''
	Use modified Kadane's algo to find the max subarray. Keep summing all the elements in some variable `max_so_far`.
	and if the value of max_so_far is bigger than max_sum, update the max_sum. The final max sum will have maximum 
	contiguous subarray. In this problem we need to calculate the maximum sum, for that just keep adding all the 
	positive values. 
'''

import math
import os
import random
import re
import sys


def maxSubarray(arr):
    max_so_far = 0
    max_sum = 0
    min_ = 0
    s = 0
    if max(arr)<min_:                # edge case if all the numbers are negative
        return [max(arr),max(arr)]
    for i in arr:
        if i>0:
            s += i
        max_so_far += i 
        if max_so_far < 0:
            max_so_far = 0
        if max_so_far > max_sum:
            max_sum = max_so_far
    return [max_sum,s]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
