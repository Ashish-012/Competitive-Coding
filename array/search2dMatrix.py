'''
	We can do binary search in a row or a column and traverse rest or the row
	and column but the complexity in such case would be O(nlogn)
	So to decrease the complexity we use ladder search approach. Initialise a pointer
	which is pointing to the last column of first row. If the number at that position is
	greater than the required number increment the row. If it is smaller than the required 
	number decrement the column.
'''
mat = [ [10, 20, 30, 40], 
        [15, 25, 35, 45], 
        [27, 29, 37, 48], 
        [32, 33, 39, 50] ] 

r = 4
c = 4
i = 0
j = c-1

find = 33  #the key we have to find

while i < r and j >= 0:
	num = mat[i][j]
	if num == find:
		print(f"Number found at index {i},{j}")
		break
	elif num > find:	
		j -= 1
	else:
		i += 1

if (i > r or j < 0):
	print('Not found')