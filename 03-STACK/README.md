## **Stack in Python**

---

### **1. What is a Stack?**

A **Stack** is a linear data structure that follows the principle:

> **LIFO – Last In, First Out**

The last element inserted is the first one to be removed.

Example (Real Life):

* Stack of plates 🍽️
* Undo / Redo operations
* Browser back button

---

### **2. Basic Stack Operations**

| Operation  | Description             |
| ---------- | ----------------------- |
| Push       | Insert element          |
| Pop        | Remove top element      |
| Peek / Top | View top element        |
| isEmpty    | Check if stack is empty |
| Size       | Number of elements      |

---

### **3. Stack Implementation Methods in Python**

1. Using **List** (Most Common)
2. Using **Collections.deque**
3. Using **Linked List**

---

## **METHOD 1: Stack Using List** ⭐

### **4. Create Stack**

```python
stack = []
```

---

### **5. Push Operation**

```python
stack.append(10)
stack.append(20)
stack.append(30)
```

---

### **6. Pop Operation**

```python
stack.pop()
```

---

### **7. Peek (Top Element)**

```python
print(stack[-1])
```

---

### **8. Check Empty Stack**

```python
if not stack:
    print("Stack is empty")
```

---

### **9. Stack Size**

```python
len(stack)
```

---

### **10. Complete Stack Using List**

```python
stack = []

stack.append(10)
stack.append(20)
stack.append(30)

print(stack)
print(stack.pop())
print(stack[-1])
print(len(stack))
```

---

## **METHOD 2: Stack Using deque (Efficient)**

```python
from collections import deque

stack = deque()
stack.append(10)
stack.append(20)
stack.append(30)
stack.pop()
```

**Why deque?**

* Faster push & pop (O(1))
* Thread-safe

---

## **METHOD 3: Stack Using Linked List** ⭐ (DSA Favorite)

### **11. Node Class**

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

---

### **12. Stack Class**

```python
class Stack:
    def __init__(self):
        self.top = None
```

---

### **13. Push Operation**

```python
def push(self, data):
    new_node = Node(data)
    new_node.next = self.top
    self.top = new_node
```

---

### **14. Pop Operation**

```python
def pop(self):
    if self.top is None:
        print("Stack Underflow")
        return
    self.top = self.top.next
```

---

### **15. Peek Operation**

```python
def peek(self):
    if self.top:
        return self.top.data
```

---

### **16. Display Stack**

```python
def display(self):
    temp = self.top
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")
```

---

### **17. Full Working Example**

```python
s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.display()
s.pop()
s.display()
```

---

### **18. Stack Overflow & Underflow**

* **Overflow**: Stack is full
* **Underflow**: Stack is empty

Occurs mostly in fixed-size stacks.

---

### **19. Time Complexity**

| Operation | Time |
| --------- | ---- |
| Push      | O(1) |
| Pop       | O(1) |
| Peek      | O(1) |

---

### **20. Applications of Stack** ⭐

* Undo / Redo
* Expression evaluation
* Parenthesis checking
* Function calls (Call Stack)
* Backtracking algorithms

---

### **21. Important Interview Problems**

* Reverse string using stack
* Valid parentheses
* Next greater element
* Infix → Postfix
* Stack using queue

---

### **22. Common Mistakes**

* Popping from empty stack
* Forgetting LIFO order
* Using list.insert(0) (slow)

---

### **23. Stack vs Queue**

| Stack   | Queue    |
| ------- | -------- |
| LIFO    | FIFO     |
| One end | Two ends |

---

### **24. Summary**

Stack is a **fundamental DSA structure** used internally by programs and heavily tested in interviews. Mastering stack builds strong logic for:

* Recursion
* Expression parsing
* Advanced algorithms

---

**Author:** NITHIN KUMAR Y 🚀
