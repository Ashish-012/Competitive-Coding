'''
	As the list is sorted, we need two pointers poining to the current and next node. We will loop till the next pointer reaches the end of the list
	Now we check if the current data is equal to the next data, if it is then iterate the next value till we reach a point where the current data
	is not equal to the next data. Now just set the link of current.next to next pointer. (We have to check the case if the next pointer reaches the
	last node and still their values are equal, so in that case set the link of the current.next to None).
'''

def removeDuplicates(head):
    if not head:
        return head
    current = head
    nxt = current.next
    while nxt:
        if current.data == nxt.data and nxt.next:
            nxt = nxt.next
        elif current.data == nxt.data and not nxt.next:
            nxt = None
            current.next = nxt
        else:
            current.next = nxt
            current = current.next
            nxt = nxt.next
    return head