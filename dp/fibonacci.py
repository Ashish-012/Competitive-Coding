'''
	Here we have a loopkup table qb. As we find the values of n'th fibonacci numbers we save them in the table so that if
	we need them again we won't have to recalculate, we can just check their corresponding value in the table. So just 
	recursively call the fibonacci function and call for the sum of n-1 and n-2th number. If we have those numbers in our 
	table we just return them otherwise we calculate them and then store them in the table.  
'''

def fibonacci(n, qb):
	if n == 0 or n == 1:    # exit condition 
		return n

	if qb[n]:				# if we have the n'th fibonacci number in the table we use it instead of calculating again
		return qb[n]

	fibn = fibonacci(n-1, qb) + fibonacci(n-2, qb)  

	qb[n] = fibn 			# if we dont have the number in our table we store it in the table

	return fibn

n = 34
qb = [None]*100
print(f'{n}th fibonacci number is',fibonacci(n, qb))
