import sys 
sys.stdin = open('in.txt', 'r')
sys.stdout = open('out.txt', 'w')

# Code from here...
class SortingAlgo:

	def bubblesort(self,arr):
		n = len(arr)

		for i in range(n):

			swap = False

			for j in range(n-1-i):
			#last element in sorted pos

				if arr[j]>arr[j+1]:
					arr[j],arr[j+1]=arr[j+1],arr[j]

					swap= True

			if not swap:
				break


		print(arr)
		#Time O(n2) worst and average

	def selectionsort(self,arr):
		#select max ind swap max index with last

		n = len(arr)

		for i in range(n):

			max_ind = n-1-i

			for j in range(n-i):

				if arr[j]>arr[max_ind]:
					max_ind=j 

			arr[max_ind],arr[n-1-i]= arr[n-1-i],arr[max_ind]

		print(arr)


	def insertionsort(self,arr):

		n = len(arr)

		for i in range(1,n):

			j=i-1
			val = arr[i]

			# Compare key with each element on the left of it...
			# until an element smaller than it is found
			while j>=0 and val<arr[j]:

				arr[j+1]=arr[j] #shift
				j-=1


			arr[j+1]=val

		print(arr)


	def mergesort(self,arr):

		n = len(arr)

		self._mergesort(arr,0,n-1)

		print(arr)


	def _mergesort(self,arr,l,r):

		if l>=r:
			return

		mid = (l+r)//2

		self._mergesort(arr, l, mid)

		self._mergesort(arr,mid+1, r)

		self._merge(arr,l,mid,r)

	def _merge(self,arr,l,mid,r):

		temp=[0]*(r-l+1)

		i,j,k=l,mid+1,0

		while i<=mid and j<=r:

			if arr[i]<=arr[j]:
				temp[k]=arr[i]
				i+=1
				k+=1 

			else:
				temp[k]=arr[j]
				k+=1
				j+=1


		while i<=mid:

			temp[k]=arr[i]
			k+=1 
			i+=1

		while j<=r:

			temp[k]=arr[j]
			k+=1
			j+=1

		for i in range(0,r-l+1):

			arr[l+i]=temp[i]
			#arr[l+0]--arr[l+r-l]

		return


	def quicksort(self,arr):

		n = len(arr)

		self._quicksort(arr,0,n-1)

		print(arr)

	def _quicksort(self,arr,l,r):

		if(l>=r):
			return

		p= self._partition(arr,l,r)

		self._quicksort(arr, l, p-1)

		self._quicksort(arr,p+1, r)


	def _partition(self,arr,l,r):

		pivot = arr[r]

		ind=l

		for i in range(l,r):

			if arr[i]<=pivot:

				arr[ind],arr[i]=arr[i],arr[ind]
				ind+=1


		arr[ind],arr[r] = arr[r],arr[ind]

		return ind 



	def heapsort(self,arr):

		 n = len(arr)

		 for i in range(n//2-1,-1,-1):#n//2-1 is last middle node rest is leaf

		 	self._heapify(arr,n,i)


		 for i in range(n-1,-1,-1):

		 	arr[0],arr[i] = arr[i],arr[0]
		 	#swap first and last then heapify 

		 	self._heapify(arr,i,0)


		 print(arr)

	def _heapify(self,arr,n,root):


		left= 2*root+1
		right = 2*root+2

		largest = root

		if(left<n and arr[left]>arr[largest]):
			largest=left 

		if(right<n and arr[right]>arr[largest]):
			largest=right 


		if largest!=root:
			arr[root],arr[largest] = arr[largest],arr[root]

			self._heapify(arr, n, largest)




if __name__ == '__main__':


	arr=[6,5,4,3,2,1]

	obj = SortingAlgo()

	obj.bubblesort(arr[:])

	obj.selectionsort(arr[:])

	obj.insertionsort(arr[:])

	obj.mergesort(arr[:])

	obj.quicksort(arr[:])

	obj.heapsort(arr[:])