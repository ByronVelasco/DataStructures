class MaxHeap:
	def __init__(self, max_size):
		# Initialize an empty list to represent the heap
		self.heap = []
		self.size = 0
		self.max_size = max_size  # Set the maximum allowed size
		self.max = None      # Attribute to store the current max value

	def __str__(self):
		# Return a string representation of the heap
		return str(self.heap)

	def _update_max(self):
		# Update the max attribute to the first element or None if empty
		self.max = self.heap[0] if not self.is_empty() else None
	
	def _sift_up(self, index):
		# Sift up the element at the given index
		parent = (index - 1) // 2
		while index > 0 and self.heap[index] > self.heap[parent]:
			# Swap the current element with its parent
			self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
			index = parent
			parent = (index - 1) // 2
		self._update_max()

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
		self._update_max()

	def is_empty(self):
		# Check if the heap is empty
		return self.size == 0

	def insert(self, value):
		# Add the new value to the end of the heap if not full (when max_size is set)
		if self.size == self.max_size:
			print("Heap is at maximum capacity. Cannot insert new value.")
			return
		self.heap.append(value)
		self.size += 1
		# Restore the max-heap property by sifting up
		self._sift_up(self.size - 1)
	
	def extract_max(self):
		if self.is_empty():
			print("Heap is empty. Cannot extract maximum.")
			return
		# Remove and return the maximum element in the heap
		maximum = self.max
		# Move the last element to the root and remove it from the heap
		self.heap[0] = self.heap[-1]
		self.heap.pop()
		self.size -= 1
		# Restore the max-heap property by sifting down
		if self.size > 0:
			self._sift_down(0)
		self._update_max()
		return maximum

	def update_value(self, old, new):
		# Check if the old value exists in the heap
		try:
			index = self.heap.index(old)
		except ValueError:
			print(f"Value {old} not found in the heap. Cannot update.")
			return
		# Update the value at the found index
		self.heap[index] = new
		# Restore the max-heap property
		if new > old:
			self._sift_up(index)
		else:
			self._sift_down(index)
			

class MinHeap(MaxHeap):
	def __init__(self, max_size):
		super().__init__(max_size)
		del self.max # Remove the max attribute from MaxHeap
		self.min = None  # Attribute to store the current min value

	def _update_min(self):
		# Update the min attribute to the first element or None if empty
		self.min = self.heap[0] if not self.is_empty() else None

	def _sift_up(self, index):
		# Sift up the element at the given index for min-heap
		parent = (index - 1) // 2
		while index > 0 and self.heap[index] < self.heap[parent]:
			self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
			index = parent
			parent = (index - 1) // 2
		self._update_min()

	def _sift_down(self, index):
		# Sift down the element at the given index for min-heap
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

			self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
			index = smallest
		self._update_min()

	def extract_min(self):
		if self.is_empty():
			print("Heap is empty. Cannot extract minimum. Cannot extract minimum.")
			return None
		minimum = self.min
		self.heap[0] = self.heap[-1]
		self.heap.pop()
		self.size -= 1
		if self.size > 0:
			self._sift_down(0)
		self._update_min()
		return minimum

	def update_value(self, old, new):
		# Check if the old value exists in the heap
		try:
			index = self.heap.index(old)
		except ValueError:
			print(f"Value {old} not found in the heap. Cannot update.")
			return
		self.heap[index] = new
		if new < old:
			self._sift_up(index)
		else:
			self._sift_down(index)


class Stack:
	def __init__(self, max_size):
		self.stack = [None] * max_size 	# Internal list to store stack elements
		self.size = 0               # Current number of elements in the stack
		self.max_size = max_size    # Maximum allowed size of the stack
		self.top = None             # The top element of the stack (None if empty)

	def __str__(self):
		return str(self.stack)

	def _update_top(self):
		self.top = self.stack[self.size - 1] if self.size > 0 else None

	def is_empty(self):
		return self.size == 0
	
	def push(self, item):
		if self.size == self.max_size:
			print("Stack is at maximum capacity. Cannot push.")
			return
		self.stack[self.size] = item
		self.size += 1
		self._update_top()

	def pop(self):
		if self.is_empty():
			print("Stack is empty. Cannot pop.")
			return None
		item = self.stack[self.size - 1]
		self.size -= 1
		self.stack[self.size] = None
		self._update_top()
		return item


class Queue:
	def __init__(self, max_size):
		self.queue = [None] * max_size
		self.max_size = max_size
		self.size = 0
		self.head_index = None
		self.tail_index = None

	def __str__(self):
		return str(self.queue)

	def is_empty(self):
		return self.size == 0

	def enqueue(self, item):
		if self.size == self.max_size:
			print("Queue is full. Cannot enqueue item.")
			return
		if self.head_index is None:
			self.head_index = 0
		self.tail_index = (self.tail_index + 1) % self.max_size if self.tail_index is not None else 0
		self.queue[self.tail_index] = item
		self.size += 1
  
	def dequeue(self):
		if self.is_empty():
			print("Queue is empty. Cannot dequeue item.")
			return
		item = self.queue[self.head_index]
		self.queue[self.head_index] = None
		self.head_index = (self.head_index + 1) % self.max_size
		self.size -= 1
		if self.size == 0:
			self.head_index = None
			self.tail_index = None
		return item

	def head(self):
		if self.is_empty():
			print("Queue is empty. No head item.")
			return
		return self.queue[self.head_index]


class NodeSLL:
	def __init__(self, key=None):
		"""Initialize a new node.
		
		Args:
				data: The data to be stored in the node.
		"""
		self.key = key      	# key stored in the node
		self.next = None      # Reference to the next node (initially None)
    
	def __str__(self) -> str:
		"""Return a string representation of the node."""
		return f"{self.key} -> {self.next.key}"


class SinglyLinkedList:
	def __init__(self):
		"""Initialize a singly linked list with a sentinel node.
		
		The sentinel node simplifies insertion and deletion operations
		by eliminating special cases for empty lists.
		"""
		self.sentinel = NodeSLL()  		# Sentinel node with no data
		self.sentinel.next = self.sentinel  # Points to itself initially
		self.size = 0               # Number of elements in the list
		self.head = None						# Head points to the first node's key (initially None)
	
	def __str__(self) -> str:
		"""Return a string representation of the linked list."""
		if self.size == 0:
			return "Empty list"
		
		result = []
		current = self.sentinel.next
		while current != self.sentinel:
			result.append(str(current.key))
			current = current.next
		return " -> ".join(result)
	
	def search(self, key) -> NodeSLL:
		"""Search for a node with the given key.
		
		Args:
			key: The key to search for.
				
		Returns:
			Node: The node containing the key, or None if not found.
		"""
		current = self.sentinel.next
		while current != self.sentinel and current.key != key:
			current = current.next
		return current
	
	def prepend(self, key) -> None:
		"""Insert a new node at the beginning of the list.
		
		Args:
			key: The key to be inserted.
		"""
		new_node = NodeSLL(key)
		new_node.next = self.sentinel.next
		self.sentinel.next = new_node
		self.head = new_node.key
		self.size += 1
	
	def insert(self, key, target_key) -> None:
		"""Insert a new node after the node with the specified key.
		
		Args:
			key: The key to be inserted.
			target_key: The key of the node after which to insert.
		"""
		# Find the target node
		current = self.search(target_key)
		if current == self.sentinel:
			print(f"Target key {target_key} not found in the list.")
			return
		
		# Insert the new node after the target node
		new_node = NodeSLL(key)
		new_node.next = current.next
		current.next = new_node
		self.size += 1
	
	def delete(self, key) -> bool:
		"""Delete the first node with the given key.
		
		Args:
			key: The key to be deleted.
				
		Returns:
			bool: True if the node was deleted, False if not found.
		"""
		current = self.sentinel
		while current.next != self.sentinel and current.next.key != key:
			current = current.next
		
		if current.next == self.sentinel:
			return False  # Key not found
		
		current.next = current.next.next
		self.size -= 1
		self.head = self.sentinel.next.key
		return True
	
	def is_empty(self) -> bool:
		"""Check if the list is empty.
		
		Returns:
			bool: True if the list is empty, False otherwise.
		"""
		return self.size == 0


class NodeDLL:
	def __init__(self, key=None):
		"""Initialize a new node for doubly linked list.
		
		Args:
			key: The data to be stored in the node.
		"""
		self.key = key        # key stored in the node
		self.next = None      # Reference to the next node (initially None)
		self.prev = None      # Reference to the previous node (initially None)
	
	def __str__(self) -> str:
		"""Return a string representation of the node."""
		return f"{self.prev.key} <- {self.key} -> {self.next.key}"


class DoublyLinkedList:
	def __init__(self):
		"""Initialize a doubly linked list with a sentinel node.
		
		The sentinel node simplifies insertion and deletion operations
		by eliminating special cases for empty lists.
		"""
		self.sentinel = NodeDLL()          # Sentinel node with no data
		self.sentinel.next = self.sentinel  # Points to itself initially
		self.sentinel.prev = self.sentinel  # Points to itself initially
		self.size = 0                   # Number of elements in the list
		self.head = None								# Head points to the first node (initially None)
	
	def __str__(self) -> str:
		"""Return a string representation of the linked list."""
		if self.size == 0:
			return "Empty list"
		
		result = []
		current = self.sentinel.next
		while current != self.sentinel:
			result.append(str(current.key))
			current = current.next
		return " <-> ".join(result)
	
	def search(self, key) -> NodeDLL:
		"""Search for a node with the given key.
		
		Args:
			key: The key to search for.
				
		Returns:
			Node: The node containing the key, or None if not found.
		"""
		current = self.sentinel.next
		while current != self.sentinel and current.key != key:
			current = current.next
		return current
	
	def prepend(self, key) -> None:
		"""Insert a new node at the beginning of the list.
		
		Args:
			key: The key to be inserted.
		"""
		new_node = NodeDLL(key)
		new_node.next = self.sentinel.next
		new_node.prev = self.sentinel
		self.sentinel.next.prev = new_node
		self.sentinel.next = new_node
		self.head = new_node.key
		self.size += 1
	
	def insert(self, key, target_key) -> None:
		"""Insert a new node after the node with the specified key.
		
		Args:
			key: The key to be inserted.
			target_key: The key of the node after which to insert.
		"""
		# Find the target node
		target_node = self.search(target_key)
		
		if target_node == self.sentinel:
			print(f"Target key {target_key} not found in the list.")
			return
		
		# Insert the new node after the target node
		new_node = NodeDLL(key)
		new_node.next = target_node.next
		new_node.prev = target_node
		target_node.next.prev = new_node
		target_node.next = new_node
		self.size += 1
	
	def delete(self, key) -> bool:
		"""Delete the first node with the given key.
		
		Args:
			key: The key to be deleted.

		Returns:
			bool: True if the node was deleted, False if not found.
		"""
		node_to_delete = self.search(key)
		
		if node_to_delete == self.sentinel:
			return False  # Key not found
		
		# Update the prev and next pointers
		node_to_delete.prev.next = node_to_delete.next
		node_to_delete.next.prev = node_to_delete.prev
		self.head = self.sentinel.next.key
		self.size -= 1
		return True
	
	def is_empty(self) -> bool:
		"""Check if the list is empty.
		
		Returns:
			bool: True if the list is empty, False otherwise.
		"""
		return self.size == 0


class BTNode:
	def __init__(self, key):
		"""Initialize a node with a key and no children or parent."""
		self.left = None
		self.right = None
		self.parent = None
		self.val = key
  
class BinaryTree:
	def __init__(self):
		"""Initialize a binary tree with no root."""
		self.root = None
  
	def __str__(self):
		"""Return a string representation of the binary tree."""
		if self.root is None:
			return "Empty tree"
		
		result = []
		self._build_string(self.root, 0, result)
		return "\n".join(result)

	def _build_string(self, node, level, result):
		"""Helper method to build string representation recursively.
		
		Args:
			node: Current node being processed.
			level: Current depth level in the tree.
			result: List to store the string lines.
		"""
		if node is None:
			return
		
		# Add current node with indentation based on level
		indent = "  " * level
		result.append(f"{indent}{node.val}")
		
		# Process left child first, then right child
		if node.left is not None:
			self._build_string(node.left, level + 1, result)
		
		if node.right is not None:
			self._build_string(node.right, level + 1, result)
	
	def insert(self, key):
		"""Insert a new node with level-order insertion (left to right, level by level).
		
		Args:
			key: The value to be inserted.
		"""
		new_node = BTNode(key)
		
		# If tree is empty, make the new node the root
		if self.root is None:
			self.root = new_node
			return
		
		# Use a queue for level-order traversal to find the insertion point
		queue = [self.root]
		
		while queue:
			current = queue.pop(0)  # Dequeue from front
			
			# Check left child
			if current.left is None:
				current.left = new_node
				new_node.parent = current
				return
			else:
				queue.append(current.left)  # Enqueue left child
			
			# Check right child
			if current.right is None:
				current.right = new_node
				new_node.parent = current
				return
			else:
				queue.append(current.right)  # Enqueue right child
    
    
class LCRSNode:
	def __init__(self, key):
		self.left_child = None
		self.right_sibling = None
		self.parent = None
		self.val = key
  
class LeftChildRightSibling:
	def __init__(self):
		"""Initialize a tree using left-child, right-sibling representation with no root."""
		self.root = None
  
	def __str__(self):
		"""Return a string representation of the entire tree."""
		if self.root is None:
			return "Empty tree"
		
		result = []
		self._build_string(self.root, 0, result)
		return "\n".join(result)

	def _build_string(self, node, level, result):
		"""Helper method to build string representation recursively.
		
		Args:
				node: Current node being processed.
				level: Current depth level in the tree.
				result: List to store the string lines.
		"""
		if node is None:
			return
		
		# Add current node with indentation based on level
		indent = "  " * level
		result.append(f"{indent}{node.val}")
		
		# Process all children (traverse siblings)
		child = node.left_child
		while child is not None:
			self._build_string(child, level + 1, result)
			child = child.right_sibling
  
	def search(self, key):
		"""Search using breadth-first (level-by-level) traversal."""
		if self.root is None:
			return None
		
		queue = [self.root]
		
		while queue:
			current = queue.pop(0)  # Dequeue from front
			
			if current.val == key:
				return current
			
			# Add all children to queue
			child = current.left_child
			while child is not None:
				queue.append(child)
				child = child.right_sibling
		
		return None

	def insert(self, parent_key, child_key):
		"""Insert a new node as a child of the specified parent.
		
		Args:
			parent_key: The key of the parent node where the child will be added.
			child_key: The key of the new child node to be inserted.
		"""
		new_node = LCRSNode(child_key)
		
		# If tree is empty, create root
		if self.root is None:
			self.root = new_node
			return
		
		# Find the parent node
		parent_node = self.search(parent_key)
		if parent_node is None:
			print(f"Parent node with key {parent_key} not found.")
			return
		
		# Set parent relationship
		new_node.parent = parent_node
		
		# If parent has no children, make this the first child
		if parent_node.left_child is None:
			parent_node.left_child = new_node
		else:
			# Add as the rightmost sibling
			current = parent_node.left_child
			while current.right_sibling is not None:
					current = current.right_sibling
			current.right_sibling = new_node