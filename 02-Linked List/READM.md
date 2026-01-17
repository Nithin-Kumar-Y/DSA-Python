## **Linked List in Python **

---

### **1. What is a Linked List?**

A **Linked List** is a linear data structure where elements (called **nodes**) are stored in non-contiguous memory locations. Each node contains:

1. **Data** – the value stored
2. **Next** – reference (link) to the next node

Unlike arrays, linked lists do **not use indexing** and are connected using pointers/references.

---

### **2. Why Linked List? (Arrays vs Linked List)**

| Feature   | Array        | Linked List     |
| --------- | ------------ | --------------- |
| Memory    | Contiguous   | Non-contiguous  |
| Size      | Fixed        | Dynamic         |
| Insertion | Costly       | Efficient       |
| Deletion  | Costly       | Efficient       |
| Access    | Fast (index) | Slow (traverse) |

---

### **3. Types of Linked Lists**

1. **Singly Linked List**
2. **Doubly Linked List**
3. **Circular Linked List**

---

## **SINGLY LINKED LIST**

### **4. Node Structure**

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

---

### **5. Linked List Class**

```python
class LinkedList:
    def __init__(self):
        self.head = None
```

---

### **6. Insertion Operations**

#### **Insert at Beginning**

```python
def insert_begin(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node
```

#### **Insert at End**

```python
def insert_end(self, data):
    new_node = Node(data)
    if self.head is None:
        self.head = new_node
        return
    temp = self.head
    while temp.next:
        temp = temp.next
    temp.next = new_node
```

#### **Insert at Position**

```python
def insert_pos(self, pos, data):
    new_node = Node(data)
    temp = self.head
    for _ in range(pos - 1):
        temp = temp.next
    new_node.next = temp.next
    temp.next = new_node
```

---

### **7. Deletion Operations**

#### **Delete from Beginning**

```python
def delete_begin(self):
    self.head = self.head.next
```

#### **Delete from End**

```python
def delete_end(self):
    temp = self.head
    while temp.next.next:
        temp = temp.next
    temp.next = None
```

#### **Delete by Value**

```python
def delete_value(self, value):
    temp = self.head
    if temp.data == value:
        self.head = temp.next
        return
    while temp.next:
        if temp.next.data == value:
            temp.next = temp.next.next
            return
        temp = temp.next
```

---

### **8. Traversal (Display)**

```python
def display(self):
    temp = self.head
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")
```

---

### **9. Search an Element**

```python
def search(self, key):
    temp = self.head
    pos = 0
    while temp:
        if temp.data == key:
            return pos
        temp = temp.next
        pos += 1
    return -1
```

---

### **10. Length of Linked List**

```python
def length(self):
    count = 0
    temp = self.head
    while temp:
        count += 1
        temp = temp.next
    return count
```

---

### **11. Reverse a Linked List** ⭐ (Important)

```python
def reverse(self):
    prev = None
    curr = self.head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    self.head = prev
```

---

### **12. Complete Working Example**

```python
ll = LinkedList()
ll.insert_end(10)
ll.insert_end(20)
ll.insert_end(30)
ll.insert_begin(5)
ll.display()
ll.reverse()
ll.display()
```

---

## **DOUBLY LINKED LIST (Concept)**

Each node has:

* Previous
* Data
* Next

```python
class DNode:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None
```

Used when:

* Backward traversal needed
* Undo / redo operations

---

## **CIRCULAR LINKED LIST (Concept)**

* Last node points to first node
* No NULL reference

Used in:

* Round-robin scheduling
* Games
* Music playlists

---

### **13. Time Complexity**

| Operation | Time |
| --------- | ---- |
| Insert    | O(1) |
| Delete    | O(1) |
| Search    | O(n) |
| Traverse  | O(n) |

---

### **14. Common Mistakes**

* Forgetting to update head
* Losing reference while reversing
* Infinite loop in circular list

---

### **15. Real-World Applications**

* Music player
* Browser history
* Train coaches
* Memory management

---

### **16. Interview Questions (Must Practice)**

* Reverse a linked list
* Detect loop in linked list
* Find middle element
* Merge two sorted linked lists
* Remove duplicates

---

### **17. Summary**

Linked List is a **core DSA concept** and favourite of interviewers. Mastering it helps you understand:

* Pointer logic
* Dynamic memory
* Advanced structures like Stack, Queue, Graph

---

**Author:** NITHIN KUMAR Y 🚀
