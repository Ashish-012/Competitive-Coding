'''
	Iterate the list to know how many elements are in the linked list. Subtract the position of the last node from the number of nodes. Now
	iterate through the list again and break if the position is same as the position of the node we want. If it is then return its data.
'''


def getNode(head, positionFromTail):
    if not head:
        return 
    count = 0
    current = head
    while current:
        current = current.next
        count+=1
    pos = count - positionFromTail 
    node = head
    count = 1
    while node:
        if count == pos:
            break
        node = node.next
        count += 1
    if count == pos :
        return node.data
    else:
        return 