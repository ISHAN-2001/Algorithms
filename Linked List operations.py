class Node():

	def __init__(self,val=0,next=None):
		self.val = val 
		self.next=next


## Linked List operations

# 1. Reverse a Linked List

def reverse(head):

	prev,after = None,None
        
	while head is not None:

		after = head.next
		head.next = prev

		prev = head
		head = after

	return prev # new head

# 2. Middle of LL

def middle(head):

	slow ,fast= head,head 

	while fast and fast.next:

		fast = fast.next.next 
		slow= slow.next 

	return slow # mid 

# 3. LL Cycle

def cycle(head):

	if not head or not head.next:
		return False

	slow ,fast =head,head 

	while fast and fast.next:

		fast = fast.next.next 
		slow = slow.next

		if fast is slow:
			return True

	return False  

# 4. Sort a LL
# use merge sort (divide into half and merge)