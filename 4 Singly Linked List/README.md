# **Singly Linked Lists**

A **Singly Linked List** is a linear data structure where elements (called nodes) are stored in a sequence, and each node contains data and a reference (or pointer) to the next node in the sequence. Unlike arrays, linked lists do not store elements in contiguous memory locations. Instead, they use pointers to connect nodes, making insertion and deletion operations more efficient at certain positions.

## Attributes

### Node Class
- `self.key`: The data stored in the node.
- `self.next`: A reference (or pointer) to the next node in the sequence, initially set to `None`.

### SinglyLinkedList Class
- `self.sentinel`: A sentinel node with no data that simplifies insertion and deletion operations by eliminating special cases for empty lists.
- `self.size`: An integer representing the current number of elements in the linked list.
- `self.head`: A reference to the first node's key, which is initially `None` until the first node is added.

## Methods
- `is_empty()`: Returns `True` if the linked list is empty, otherwise `False`.
- `search(key)`: Searches for a node with the given key and returns the node if found, otherwise returns `None`.
- `prepend(key)`: Inserts a new node with the given key at the beginning of the linked list.
- `insert(key, target_key)`: Inserts a new node with the given key after the node containing the target key. If the target key is not found, it warns and does not insert.
- `delete(key)`: Removes the first node with the given key from the linked list. Returns `True` if the node was deleted, `False` if not found.

## Time Complexity
| Operation        | Time Complexity |
|------------------|-----------------|
| Search           | O(n)            |
| Prepend          | O(1)            |
| Insert           | O(1)            |
| Delete           | O(1)            |
| Check emptiness  | O(1)            |

- **Search** operation is O(n) because it may require traversing the entire linked list to find the target node.
- **Insert**, and **Delete** operations are O(1) when you have a pointer to the node where the operation should occur, as they involve updating pointers without needing to traverse the list.
- **Prepend** operation is O(1) because it involves adding an element at the beginning of the list without needing to traverse the structure.
- **Check emptiness** operation is O(1) because it simply checks the size of the linked list without modifying

## Applications
Singly Linked Lists are widely used in various applications, including:
- **Dynamic Memory Allocation**: Managing memory blocks where the size of data is not known in advance and can grow or shrink during runtime.
- **Implementation of Other Data Structures**: Serving as the foundation for implementing stacks, queues, and hash tables with separate chaining.
- **Undo Functionality**: Storing a sequence of operations in applications like text editors where each node represents a state that can be reverted.
- **Music Playlists**: Managing songs in a playlist where new songs can be added or removed dynamically without requiring a fixed-size array.
- **Browser History**: Maintaining a list of visited web pages where navigation between pages requires efficient insertion and deletion operations.

---
© 2025 Byron Velasco