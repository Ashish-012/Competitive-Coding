'''
	Create a new node same as head node. Now iterate through and print all the data in the list till the node is not `None`.  
'''

def printLinkedList(head):
    current  = head
    while current:
        print(current.data)
        current = current.next