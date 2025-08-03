# **Binary Tree**

A **Binary Tree** is a hierarchical data structure where each node has at most two children, referred to as the left child and the right child. The topmost node is called the root, and nodes with no children are called leaves. Binary trees are fundamental structures in computer science and serve as the foundation for more specialized tree types.

## Key Properties:
- Each node can have 0, 1, or 2 children
- There is exactly one path from the root to any node
- The structure is recursive: each subtree is also a binary tree

## Insertion Rules:

### Complete Binary Tree (Used in this implementation):
In this exercise, we follow the **complete binary tree** insertion rule:
- Fill the tree **level by level** from top to bottom
- Within each level, fill positions from **left to right**
- This ensures the tree remains balanced and compact
- Useful for heap implementations and priority queues

### Other Common Insertion Rules:
- **Binary Search Tree (BST)**: Insert nodes based on sorted values (left < parent < right)
- **AVL Tree**: Self-balancing BST that maintains height balance
- **Red-Black Tree**: Self-balancing BST with color properties
- **Random Insertion**: Insert at random positions for certain algorithms

The choice of insertion rule depends on the specific use case and the operations you need to optimize (searching, insertion, deletion, etc.).

## Attributes

### Node Class
- `self.left`: A reference (or pointer) to the left child node, initially set to None.
- `self.right`: A reference (or pointer) to the right child node, initially set to None.
- `self.parent`: A reference (or pointer) to the parent node, initially set to None.
- `self.val`: The data stored in the node.

### BinaryTree Class
- `self.root`: A reference to the root node of the binary tree, initially set to None for an empty tree.

## Methods
- `insert(key)`: Inserts a new node with the given key using level-order insertion (complete binary tree property). Fills the tree level by level from left to right.

## Time Complexity
| Operation        | Time Complexity |
|------------------|-----------------|
| Insert           | O(n)            |

- **Insert** operation is O(n) because it uses level-order traversal (BFS) to find the correct insertion position, potentially visiting all nodes in the worst case.

## Applications
Binary Trees are widely used in various applications, including:
- **File Systems**: Organizing directories and files in hierarchical structures where each folder can contain subfolders and files, enabling efficient navigation and search operations.
- **Expression Parsing**: Representing mathematical and logical expressions where operators are internal nodes and operands are leaves, facilitating evaluation and manipulation of complex expressions.
- **Database Indexing**: Implementing B-trees and other tree-based indexes for efficient data retrieval and range queries in database management systems.
- **Heap Implementation**: Serving as the underlying structure for priority queues and heap data structures used in algorithms like Dijkstra's shortest path and heap sort.
- **Decision Trees**: Modeling decision-making processes in machine learning and artificial intelligence where each internal node represents a decision point and leaves represent outcomes.
- **Huffman Coding**: Implementing data compression algorithms where frequently used characters are assigned shorter codes based on their position in the binary tree structure.

# **Left Child Right Sibling Tree**

The **Left-child, right-sibling representation** is an efficient way to represent trees with an arbitrary number of children per node using only two pointers per node. This representation transforms any tree into a binary tree structure while preserving the original tree's hierarchical relationships.

## Key Concepts:

### How it works:
- **Left pointer (`left_child`)**: Points to the first (leftmost) child of the current node
- **Right pointer (`right_sibling`)**: Points to the next sibling of the current node
- **Parent pointer (`parent`)**: Maintains the parent-child relationship for easy traversal

### Advantages:
- **Memory efficient**: Uses only two pointers regardless of the number of children
- **Flexible**: Can represent trees with any number of children per node
- **Binary tree algorithms**: Can apply binary tree algorithms to general trees
- **Easy traversal**: Supports both depth-first and breadth-first traversals

## Insertion Rules:

### Current Implementation (Parent-based insertion):
In this exercise, we follow a **parent-based insertion rule**:
- Each new node requires a **specific parent** identified by its key
- The algorithm **searches for the parent** using breadth-first search (BFS) to find the first occurrence of the parent key
- The new child is added as the **rightmost sibling** among existing children
- If the parent has no children, the new node becomes the **first child**

### Other Common Insertion Rules:
- **Level-order insertion**: Insert nodes level by level, filling positions from left to right
- **Alphabetical insertion**: Insert children in alphabetical order of their keys
- **Priority-based insertion**: Insert based on priority values or specific ordering criteria
- **Position-specific insertion**: Insert at a specific position among siblings

The choice of insertion rule depends on the application requirements and the desired tree structure for optimal performance in specific operations.

## Atributes

### Node Class
- `self.left_child`: A reference (or pointer) to the left child node, initially set to None.
- `self.right_sibling`: A reference (or pointer) to the right sibling node, initially set to None.
- `self.parent`: A reference (or pointer) to the parent node, initially set to None.
- `self.val`: The data stored in the node.

### LeftChildRightSibling Class
- `self.root`: A reference to the root node of the left-child right-sibling tree, initially set to None for an empty tree.

## Methods
- `insert(key, parent_key)`: Inserts a new node with the given key as a child of the specified parent node identified by `parent_key`. Uses breadth-first search to find the parent and adds the new node as the rightmost sibling.

## Time Complexity
| Operation        | Time Complexity |
|------------------|-----------------|
| Insert           | O(n)            |

- **Insert** operation is O(n) because it uses breadth-first search (BFS) to find the correct parent node, potentially visiting all nodes in the worst case.

## Applications
Left-child right-sibling trees are useful in various applications, including:
- **Hierarchical Data Representation**: Efficiently representing trees with arbitrary numbers of children, such as organizational charts, file systems, and XML/HTML document structures.
- **Tree Traversal Algorithms**: Applying binary tree traversal algorithms to general trees, enabling depth-first and breadth-first traversals without needing to modify the original tree structure.
- **Memory Optimization**: Reducing memory overhead by using only two pointers per node, making it suitable for large trees with many children.