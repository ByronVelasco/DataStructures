# **Stacks**

A **Stack** is a linear data structure that follows the Last-In, First-Out (LIFO) principle. This means that the last element added to the stack is the first one to be removed. For example, think of a stack of plates where you can only add or remove the top plate.

## Attributes
- `self.stack`: A list that holds the elements of the stack.
- `self.size`: An integer representing the current number of elements in the stack.
- `self.max_size`: An integer representing the maximum size of the stack, which is useful for initializing the stack with a fixed capacity. Setting this to `None` (by default) allows for dynamic resizing.
- `self.top`: An integer representing the top element of the stack, which is updated whenever an element is pushed or popped.

## Public Methods
- `is_empty()`: Returns `True` if the stack is empty, otherwise `False`.
- `push(value)`: Adds a new element to the top of the stack. If `self.max_size` is set, it checks if the stack has reached its maximum size before pushing.
- `pop()`: Removes and returns the top element from the stack. If the stack is empty, shows an message indicating that the stack is empty.

## Private Methods
- `_update_top()`: Updates the `top` attribute to the current top element of the stack.

## Time Complexity
| Operation   | Time Complexity |
|-------------|-----------------|
| Push        | O(1)            |
| Pop         | O(1)            |
| Check emptiness | O(1)            |

- **Push** and **pop** operations are constant time since they only involve adding or removing the top element.
- **Checking if the stack is empty** is also a constant-time operation.

## Applications
Stacks are widely used in various applications due to their LIFO nature. Some common use cases include:
- **Function Call Management:** Stacks are used to manage function calls in programming languages, where each function call is pushed onto the stack, and when it returns, it is popped off the stack.
- **Expression Evaluation:** Stacks are used in parsing and evaluating expressions, such as converting infix expressions to postfix or prefix notation.
- **Backtracking Algorithms:** Stacks are used in algorithms that require backtracking, such as depth-first search (DFS) in graphs or tree traversals.
- **Undo Mechanisms:** Stacks are used in applications that require an undo feature, where each action is pushed onto the stack, and when the user wants to undo an action, it is popped off the stack.
- **Memory Management:** Stacks are used in memory management for allocating and deallocating memory in a last-in, first-out manner.

---
© 2025 Byron Velasco