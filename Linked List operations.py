import sys
sys.stdin = open('in.txt', 'r')
sys.stdout = open('out.txt', 'w')

# Start coding..
class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

class LinkedList:
	#Write all functions here...
	def __init__(self):
		self.head = None

	def append(self,new_data):

		new_node = Node(new_data)

		if(self.head==None):  #if list is empty
			self.head=new_node
			return

		temp = self.head

		while(temp.next != None):
			temp =temp.next

		temp.next = new_node
		

	def printList(self):

		temp = self.head
		while(temp):
			print(temp.data,end=" ")
			temp = temp.next


if __name__ == "__main__":

	llist = LinkedList()

	for _ in range(8):
		x= int(input())
		llist.append(x)

	llist.printList()




