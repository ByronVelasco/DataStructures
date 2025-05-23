# **Heaps**

## **1. Max Heap**

A **Max Heap** is a binary heap data structure where the parent node is always greater than or equal to its child nodes. This ensures that the largest element is always at the root of the heap, making it efficient for priority queue operations where quick access to the maximum element is required.

### Attributes

- `self.heap`: A list that maintains the max heap property, where each parent node is greater than or equal to its children.
- `self.size`: An integer representing the current number of elements in the heap.

### Public Methods

- `is_empty()`: Returns `True` if the heap is empty, otherwise `False`.
- `insert(value)`: Inserts a new element into the heap while maintaining the max heap property.
- `priority()`: Returns the maximum element (the root) of the heap without removing it.
- `extract_priority()`: Removes and returns the maximum element from the heap, maintaining the max heap property.
- `index(value)`: Returns the index of the specified value in the heap, or `None` if the value is not found.
- `update_value(old, new)`: Updates an element with the specified old value to a new value, ensuring the max heap property is preserved.

### Private methods

- `_sift_up(index)`: Moves the element at the given index up the heap until the max heap property is restored.
- `_sift_down(index)`: Moves the element at the given index down the heap until the max heap property is restored.

These methods are essential for maintaining the heap property after any operation that modifies the structure or values of the heap.

### Time Complexity

| Operation             | Time Complexity |
|-----------------------|----------------|
| Insertion             | O(log n)       |
| Extract Max (Root)    | O(log n)       |
| Get Max (Priority)    | O(1)           |
| Update Value          | O(n + log n)   |
| is_empty()            | O(1)           |
| Search (by value)     | O(n)           |

- **Insertion** and **extraction** require reordering the heap, which takes logarithmic time.
- **Getting the maximum** element is always O(1) since it is at the root.
- **Updating a value** requires searching for the value (O(n)), then sifting up or down (O(log n)), so the total is O(n + log n).
- **Checking if the heap is empty** is a constant-time operation.
- **Searching for a value** (not by priority) is linear, as the heap does not guarantee order except for the heap property.

## **2. Min Heap**

A **Min Heap** is a binary heap data structure where the parent node is always less than or equal to its child nodes. This property ensures that the smallest element is always at the root of the heap, making it efficient for priority queue operations where quick access to the minimum element is required.

### Attributes

- `self.heap`: A list that maintains the min heap property, where each parent node is less than or equal to its children.
- `self.size`: An integer representing the current number of elements in the heap.

### Public Methods

- `is_empty()`: Returns `True` if the heap is empty, otherwise `False`.
- `insert(value)`: Inserts a new element into the heap while maintaining the min heap property.
- `priority()`: Returns the minimum element (the root) of the heap without removing it.
- `extract_priority()`: Removes and returns the minimum element from the heap, maintaining the min heap property.
- `index(value)`: Returns the index of the specified value in the heap, or `None` if the value is not found.
- `update_value(old, new)`: Updates an element with the specified old value to a new value, ensuring the min heap property is preserved.

### Time Complexity

| Operation             | Time Complexity |
|-----------------------|----------------|
| Insertion             | O(log n)       |
| Extract Min (Root)    | O(log n)       |
| Get Min (Priority)    | O(1)           |
| Update Value          | O(n + log n)   |
| is_empty()            | O(1)           |
| Search (by value)     | O(n)           |

- **Insertion** and **extraction** require reordering the heap, which takes logarithmic time.
- **Getting the minimum** element is always O(1) since it is at the root.
- **Updating a value** requires searching for the value (O(n)), then sifting up or down (O(log n)), so the total is O(n + log n).
- **Checking if the heap is empty** is a constant-time operation.
- **Searching for a value** (not by priority) is linear, as the heap does not guarantee order except for the heap property.

---
© 2025 Byron Velasco