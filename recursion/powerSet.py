'''
	Initialize current by null string and index by 0. Then recursively call the function by including the element at that index and 
	excluding the element at that index. If we are at the leaf that means index has reached the length of string, print the nodes and
	return.

'''


def powerSet(s,current='',index=0):
	if index == len(s):
		print(current)
		return
	powerSet(s,current,index+1)
	powerSet(s,current + s[index],index+1)

powerSet("ABC")