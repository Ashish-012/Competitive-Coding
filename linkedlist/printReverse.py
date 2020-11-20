'''
	We can do this both recursively or iteratively. 
	In the recursive way we recursively call head.next till it is not None. After that we print the data. So after all the recursive calls
	the last node will be printed first then second last and so on...	

	In the iterative way we traverse the list storing the data in a list and in the end
	print the list in reverse.
'''

def reversePrint(head):
    if head.next:
        reversePrint(head.next)
    print(head.data)


# def reversePrint(head):
#     l = []
#     if not head:
#         return 
#     current = head
#     while current:
#         l.append(current.data)
#         current = current.next
#     for i in range(len(l)-1,-1,-1):
#         print(l[i])