class MaxHeap:
	def __init__(self):
		# Initialize an empty list to represent the heap
		self.heap = []
		self.size = 0

	def __str__(self):
		# Return a string representation of the heap
		return str(self.heap)
	
	def _sift_up(self, index):
		# Sift up the element at the given index
		parent = (index - 1) // 2
		while index > 0 and self.heap[index] > self.heap[parent]:
			# Swap the current element with its parent
			self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
			index = parent
			parent = (index - 1) // 2

	def _sift_down(self, index):
		# Sift down the element at the given index
		while True:
			left = 2 * index + 1
			right = 2 * index + 2
			largest = index

			if left < self.size and self.heap[left] > self.heap[largest]:
				largest = left
			if right < self.size and self.heap[right] > self.heap[largest]:
				largest = right

			if largest == index:
				break

			# Swap the current element with the largest child
			self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
			index = largest

	def is_empty(self):
		# Check if the heap is empty
		return self.size == 0

	def insert(self, value):
		# Add the new value to the end of the heap
		self.heap.append(value)
		self.size += 1
		# Restore the max-heap property by sifting up
		self._sift_up(self.size - 1)
		
	def priority(self):
		# Return the maximum element in the heap
		if self.is_empty():
			return None
		return self.heap[0]
	
	def extract_priority(self):
		# Remove and return the maximum element in the heap
		if self.is_empty():
			return None
		priority = self.priority()
		# Move the last element to the root and remove it from the heap
		self.heap[0] = self.heap[-1]
		self.heap.pop()
		self.size -= 1
		# Restore the max-heap property by sifting down
		self._sift_down(0)
		return priority
	
	def index(self, value):
		# Return the index of the given value in the heap
		try:
			return self.heap.index(value)
		except ValueError:
			return None

	def update_value(self, old, new):
		# Check if the old value exists in the heap
		index = self.index(old)
		if index is None:
			print(f"Value {old} not found in the heap.")
			return
		# Update the value at the found index
		self.heap[index] = new
		# Restore the max-heap property
		if new > old:
			self._sift_up(index)
		else:
			self._sift_down(index)
			

class MinHeap(MaxHeap):
	"""
	Inherited methods:
		- index(value): Returns the index of a given value in the heap.
		- priority(): Returns the minimum element in the heap.
		- extract_priority(): Removes and returns the minimum element from the heap.
	"""

	def _sift_up(self, index):
		# Sift up the element at the given index for min-heap
		parent = (index - 1) // 2
		while index > 0 and self.heap[index] < self.heap[parent]:
			# Swap the current element with its parent
			self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
			index = parent
			parent = (index - 1) // 2

	def _sift_down(self, index):
		# Sift down the element at the given index for min-heap
		self.size
		while True:
			left = 2 * index + 1
			right = 2 * index + 2
			smallest = index

			if left < self.size and self.heap[left] < self.heap[smallest]:
				smallest = left
			if right < self.size and self.heap[right] < self.heap[smallest]:
				smallest = right

			if smallest == index:
				break

			# Swap the current element with the smallest child
			self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
			index = smallest

	def update_value(self, old, new):
		# Check if the old value exists in the heap
		index = self.index(old)
		if index is None:
			print(f"Value {old} not found in the heap.")
			return
		# Update the value at the found index
		self.heap[index] = new
		# Restore the min-heap property
		if new > old:
			self._sift_down(index)
		else:
			self._sift_up(index)
			

