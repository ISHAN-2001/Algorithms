class Node:

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
class Solution:
    
    # merge sort
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        
        # middle element
        slow,fast,prev  = head,head,None
        
        
        while fast and fast.next:
            prev=slow
            fast = fast.next.next
            slow= slow.next
            
        mid = prev
        midnext = prev.next
        mid.next = None
        
        l1 = self.sortList(head)
        l2 = self.sortList(midnext)
        
        l3 = self.merge(l1,l2)
        
        return l3
    
    def merge(self,l1,l2):
        
        head = ListNode(-1)
        l3 = head
        
        while l1 and l2:
            
            if l1.val <= l2.val:
                l3.next = ListNode(l1.val)
                l1=l1.next
                l3=l3.next
                
            else:
                l3.next = ListNode(l2.val)
                l2=l2.next
                l3=l3.next
                
        l3.next = l1 if l1 else l2
            
        return head.next