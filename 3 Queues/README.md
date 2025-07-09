# **Queues**

A **Queue** is a linear data structure that follows the First-In, First-Out (FIFO) principle. This means that the first element added to the queue is the first one to be removed. For example, think of a line of people waiting at a store where the first person in line is the first one to be served.

## Attributes
- `self.queue`: A list that holds the elements of the queue.
- `self.size`: An integer representing the current number of elements in the queue.
- `self.max_size`: An integer representing the maximum size of the queue, which is useful for initializing the queue with a fixed capacity.
- `self.head_index`: An integer representing the index of the front element of the queue, which is updated whenever an element is enqueued or dequeued.
- `self.tail_index`: An integer representing the index of the last element in the queue, which is updated whenever an element is enqueued.

## Public Methods
- `is_empty()`: Returns `True` if the queue is empty, otherwise `False`.
- `enqueue(item)`: Adds an item to the end of the queue. If the queue is full, it warns that the queue is full and does not add the item.
- `dequeue()`: Removes and returns the item at the front of the queue. If the queue is empty, it warns that the queue is empty and does not remove any item.
- `head()`: Returns the item at the front of the queue without removing it. If the queue is empty, it warns that the queue is empty and returns `None`.

## Time Complexity
| Operation   | Time Complexity |
|-------------|-----------------|
| Enqueue     | O(1)            |
| Dequeue     | O(1)            |
| Check emptiness | O(1)        |
| Show head   | O(1)            |

- **Enqueue** and **Dequeue** operations are O(1) because they involve adding or removing an element from the front or back of the queue without needing to traverse the entire structure.
- **Check emptiness** and **Show head** operations are also O(1) because they simply check the state of the queue or return the front element without modifying the queue.

## Applications
Queues are widely used in various applications, including:
- **Task Scheduling**: Managing tasks in operating systems where processes are scheduled in the order they arrive.
- **Breadth-First Search (BFS)**: In graph algorithms, queues are used to explore nodes level by level.
- **Print Spooling**: Managing print jobs in a printer queue where the first job submitted is the first to be printed.

---
© 2025 Byron Velasco