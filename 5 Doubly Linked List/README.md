# **Doubly Linked Lists**

A **Doubly Linked List** is a linear data structure where elements (called nodes) are stored in a sequence, and each node contains data and two references (or pointers) - one to the next node and another to the previous node in the sequence. Unlike singly linked lists, doubly linked lists allow bidirectional traversal, making it possible to move both forward and backward through the list. This bidirectional capability makes insertion and deletion operations more efficient at any position since you can access both neighboring nodes directly.

## Attributes

### Node Class
- `self.key`: The data stored in the node.
- `self.next`: A reference (or pointer) to the next node in the sequence, initially set to `None`.
- `self.prev`: A reference (or pointer) to the previous node in the sequence, initially set to `None`.

### DoublyLinkedList Class
- `self.sentinel`: A circular sentinel node with no data that points to itself initially. It simplifies insertion and deletion operations by eliminating special cases for empty lists.
- `self.size`: An integer representing the current number of elements in the linked list.
- `self.head`: A reference to the first node's key, which is initially `None` until the first node is added.

## Methods
- `is_empty()`: Returns `True` if the linked list is empty, otherwise `False`.
- `search(key)`: Searches for a node with the given key and returns the node if found (returns the sentinel node if not found).
- `prepend(key)`: Inserts a new node with the given key at the beginning of the linked list.
- `insert_after(key, target_key)`: Inserts a new node with the given key after the node containing the target key. If the target key is not found, it warns and does not insert.
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
Doubly Linked Lists are widely used in various applications, including:
- **Browser History**: Implementing forward and backward navigation in web browsers where users can move both directions through their browsing history efficiently.
- **Undo/Redo Functionality**: Managing operation history in text editors and applications where users need to move back and forth through their actions.
- **Implementation of Deques (Double-Ended Queues)**: Serving as the foundation for data structures that require efficient insertion and deletion at both ends.
- **Music Player Applications**: Managing playlists with previous/next song functionality, allowing users to navigate bidirectionally through their music library.
- **LRU (Least Recently Used) Cache**: Implementing cache replacement policies where recently accessed items need to be moved efficiently within the cache structure.
- **Memory Management**: Managing free memory blocks in operating systems where adjacent blocks need to be merged or split efficiently.

---
© 2025 Byron Velasco