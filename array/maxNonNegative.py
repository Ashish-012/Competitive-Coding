'''
	Maintain two lists and two integers to store the max sum and current sum and their indexes.
	Now iterate through the array and keep adding to the current sum and current sum list if the
	number is positive. If the current sum is greater than max sum then update the values of
	max sum and max sum list. If we get to a negative number remove all the things from current sum 
	and current sum list. 
'''


def maxset(A):
    current_sum_list = []
    max_sum_list = []
    current_sum = 0
    max_sum = 0
    for i in A:
        if i >= 0:
            current_sum += i
            current_sum_list.append(i)
            
            if max_sum < current_sum:
                max_sum = current_sum
                max_sum_list = current_sum_list
            elif current_sum == max_sum:
                if len(current_sum_list) > len(max_sum_list):
                    max_sum_list = current_sum_list
        elif i < 0:
            current_sum = 0
            current_sum_list = []
    return max_sum_list
    
    