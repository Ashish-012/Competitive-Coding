''' Use `Counter` to make a hashmap which will store frequency of each element.
 	Check the value, if it is not divisible by 2 then it is repeated odd 
	number of times.

	Another good solution will be to take XOR of all the elements in the array
	and the remaining element will be the one present odd number of times. 
'''

from collections import Counter

t = int(input())
arr = list(map(int, input().split()))
d = Counter(arr)

for key,value in d.items():
    if value % 2 != 0:
        print(key)
        break