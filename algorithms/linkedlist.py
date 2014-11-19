
class Node(object):
	def __init__(self, val, next=None):
		self.val = val
		self.next = next

def delete_node(head, val):
	before = None
	if head.val == val:
		head = head.next
	else:
		curr = head
		while curr != None and curr.val != val:
			before = curr
			curr = curr.next
		if curr != None:
			before.next = curr.next
	return head