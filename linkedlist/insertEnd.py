'''
	Check if the head is None. If it is then the list is empty, simply point head to the new node and return it. Otherwise iterate 
	through the list till the next element is not None. Now make the last node point to the new node we created.
'''

def insertNodeAtTail(head, data):
    node = SinglyLinkedListNode(data)
    if not head:
        head = node
        return head
    current = head
    while current.next:
        current = current.next
    current.next = node
    return head