'''
	Use three pointers. One to point at the current node, one to point at previous and one for the next. Increment current till we reach the 
	end of the list(Iterate the linked list). Set the nxt node to point at the current.next node (so that we wont lose it after setting up 
	different link), then update the next link of the current node to previous node of reverse the list. Now increment both previous and current 
	node. In the end set the head of the node to the prev node which will now point to the head of the linked list.
'''


def reverse(head):
    prev = None
    current = head
    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    head = prev
    return head