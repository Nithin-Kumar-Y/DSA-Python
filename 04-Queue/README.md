## **Queue in Python**

---

### **1. What is a Queue?**

A **Queue** is a linear data structure that follows the principle:

> **FIFO – First In, First Out**

The element inserted first is removed first.

Real-life examples:

* People standing in a line
* Printer job scheduling
* Ticket booking system

---

### **2. Basic Queue Operations**

| Operation | Description               |
| --------- | ------------------------- |
| Enqueue   | Insert element at rear    |
| Dequeue   | Remove element from front |
| Front     | View front element        |
| Rear      | View last element         |
| isEmpty   | Check if queue is empty   |
| Size      | Number of elements        |

---

### **3. Types of Queues**

1. Simple Queue
2. Circular Queue
3. Priority Queue
4. Deque (Double Ended Queue)

---

## **QUEUE USING LIST (Basic Concept)**

### **4. Create Queue**

```python
queue = []
```

---

### **5. Enqueue Operation**

```python
queue.append(10)
queue.append(20)
queue.append(30)
```

---

### **6. Dequeue Operation** ⚠️ (Slow)

```python
queue.pop(0)
```

**Note:** Removing from front is **O(n)** in list.

---

## **QUEUE USING collections.deque (Recommended)** ⭐

### **7. Create Queue**

```python
from collections import deque

queue = deque()
```

---

### **8. Enqueue**

```python
queue.append(10)
queue.append(20)
```

---

### **9. Dequeue**

```python
queue.popleft()
```

---

### **10. Front & Rear Elements**

```python
print(queue[0])     # Front
print(queue[-1])    # Rear
```

---

### **11. Queue Size & Empty Check**

```python
len(queue)

if not queue:
    print("Queue is empty")
```

---

### **12. Complete Working Example**

```python
from collections import deque

q = deque()
q.append(10)
q.append(20)
q.append(30)

print(q.popleft())
print(q)
```

---

## **QUEUE USING LINKED LIST (DSA IMPORTANT)** ⭐

### **13. Node Class**

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

---

### **14. Queue Class**

```python
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
```

---

### **15. Enqueue Operation**

```python
def enqueue(self, data):
    new_node = Node(data)
    if self.rear is None:
        self.front = self.rear = new_node
        return
    self.rear.next = new_node
    self.rear = new_node
```

---

### **16. Dequeue Operation**

```python
def dequeue(self):
    if self.front is None:
        print("Queue Underflow")
        return
    self.front = self.front.next
    if self.front is None:
        self.rear = None
```

---

### **17. Display Queue**

```python
def display(self):
    temp = self.front
    while temp:
        print(temp.data, end=" <- ")
        temp = temp.next
    print("None")
```

---

### **18. Full Example (Linked List Queue)**

```python
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
q.dequeue()
q.display()
```

---

## **CIRCULAR QUEUE (Concept)**

* Rear connects back to front
* Efficient memory usage
* Avoids space wastage

Used in:

* CPU scheduling
* Streaming buffers

---

## **DEQUE (Double Ended Queue)**

* Insert/delete from both ends

```python
from collections import deque

dq = deque()
dq.append(10)
dq.appendleft(5)
dq.pop()
dq.popleft()
```

---

### **19. Time Complexity**

| Operation  | Time |
| ---------- | ---- |
| Enqueue    | O(1) |
| Dequeue    | O(1) |
| Front/Rear | O(1) |

---

### **20. Applications of Queue** ⭐

* CPU scheduling
* Breadth First Search (BFS)
* Printer queue
* Network packet handling
* Order processing systems

---

### **21. Common Mistakes**

* Using list.pop(0)
* Forgetting to update rear
* Queue underflow

---

### **22. Queue vs Stack**

| Queue    | Stack   |
| -------- | ------- |
| FIFO     | LIFO    |
| Two ends | One end |

---

### **23. Interview Questions**

* Implement queue using stack
* Circular queue implementation
* First non-repeating character
* Sliding window problems

---

### **24. Summary**

Queue is a fundamental data structure widely used in system design, scheduling, and graph algorithms. Strong understanding of queue helps in mastering:

* BFS
* OS concepts
* Real-time systems

---

**Author:** NITHIN KUMAR Y 🚀
