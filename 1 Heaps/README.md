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

### Applications

Max Heaps are widely used in various fields and applications where efficient access to the largest element is required. Some common use cases include:

- **Priority Queues:** Max Heaps are the underlying data structure for priority queues, where elements with higher priority (larger values) are served before others. This is useful in operating systems for task scheduling, bandwidth management, and simulation systems.
- **Heap Sort:** Max Heaps are used to implement the Heap Sort algorithm, an efficient comparison-based sorting technique with O(n log n) time complexity.
- **Graph Algorithms:** In algorithms like Dijkstra’s shortest path (for finding the longest path in some variations) and Prim’s algorithm (for maximum spanning trees), Max Heaps can be used to efficiently select the next vertex with the highest priority.
- **Real-Time Systems:** Max Heaps help manage resources and tasks that require immediate attention based on their priority.
- **Data Stream Processing:** Max Heaps are used to maintain the top-k largest elements in a dynamically updating dataset, such as finding the k largest numbers in a stream.
- **Load Balancing:** In distributed systems, Max Heaps can help assign tasks to the most capable servers by always selecting the server with the highest available capacity.

Max Heaps are especially useful in any context where you need to repeatedly access, insert, or remove the largest element efficiently.

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

### Applications

Min Heaps are widely used in scenarios where efficient access to the smallest element is required. Common applications include:

- **Priority Queues:** Min Heaps are the foundation for priority queues where elements with the lowest value (highest priority) are served first. This is useful in operating systems for process scheduling, event-driven simulations, and bandwidth management.
- **Heap Sort:** Min Heaps can be used to implement Heap Sort, allowing for efficient sorting of elements in descending order.
- **Graph Algorithms:** Algorithms such as Dijkstra’s shortest path and Prim’s minimum spanning tree use Min Heaps to efficiently select the next vertex with the smallest weight or cost.
- **Event Management:** In simulations and real-time systems, Min Heaps help manage events by always processing the event with the earliest timestamp or lowest priority value.
- **Data Stream Processing:** Min Heaps are used to maintain the k smallest elements in a dynamically updating dataset, such as finding the k smallest numbers in a stream.
- **Merging Sorted Lists:** Min Heaps are used in algorithms that merge multiple sorted lists or arrays, such as in external sorting or database query processing.

Min Heaps are especially useful in any context where you need to repeatedly access, insert, or remove the smallest element efficiently.

---
© 2025 Byron Velasco