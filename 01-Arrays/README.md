# Arrays (Data Structure)

## **1. Introduction to Arrays**

An **Array** is a linear data structure that stores elements of the **same data type** in a **contiguous memory location**. Each element can be accessed directly using its **index**, making arrays one of the fastest data structures for data access.

In Python, arrays are commonly implemented using **lists**, which provide dynamic sizing and rich built-in operations. For DSA learning, Python lists are sufficient to understand array concepts.

---

## **2. Why Do We Need Arrays?**

Arrays help us:

* Store multiple values under a single variable name
* Access elements quickly using index
* Perform bulk operations efficiently
* Build other data structures like stacks, queues, and matrices

### Real-World Examples

* Marks of students
* Daily temperature readings
* Cricket scores of players
* Sensor data

---

## **3. Characteristics of Arrays**

* Fixed order of elements
* Index-based access (0-based indexing)
* Fast read operations
* Same type of elements (conceptually)
* Stored sequentially in memory (conceptually)

---

## **4. Array Representation**

Example array:

```
Index:   0   1   2   3   4
Value:  10  20  30  40  50
```

Accessing an element:

```python
arr = [10, 20, 30, 40, 50]
print(arr[2])  # Output: 30
```

---

## **5. Creating Arrays in Python**

```python
arr = [1, 2, 3, 4, 5]
empty_arr = []
```

---

## **6. Basic Operations on Arrays**

### 6.1 Traversal

```python
for element in arr:
    print(element)
```

---

### 6.2 Insertion

```python
arr.append(6)        # Insert at end
arr.insert(2, 10)    # Insert at index 2
```

---

### 6.3 Deletion

```python
arr.pop()        # Delete last element
arr.pop(1)       # Delete element at index
arr.remove(10)   # Delete by value
```

---

### 6.4 Update

```python
arr[0] = 100
```

---

### 6.5 Searching

```python
if 30 in arr:
    print("Found at index", arr.index(30))
```

---

## **7. Time and Space Complexity**

| Operation           | Time Complexity |
| ------------------- | --------------- |
| Access by index     | O(1)            |
| Traversal           | O(n)            |
| Insertion at end    | O(1)*           |
| Insertion at middle | O(n)            |
| Deletion            | O(n)            |
| Searching           | O(n)            |

`*` Amortized time

---

## **8. Advantages of Arrays**

* Fast access using index
* Simple and easy to use
* Efficient memory usage
* Foundation of many algorithms

---

## **9. Limitations of Arrays**

* Fixed size (conceptually)
* Insertion and deletion are costly
* Not suitable for frequent size changes

---

## **10. Common Array Problems (DSA)**

* Find the largest and smallest element
* Reverse an array
* Find duplicate elements
* Rotate array
* Find missing number
* Kadane’s Algorithm (Maximum Subarray Sum)

---

## **11. Arrays in Python vs Traditional Arrays**

| Feature     | Python List | Traditional Array |
| ----------- | ----------- | ----------------- |
| Size        | Dynamic     | Fixed             |
| Data type   | Mixed       | Same type         |
| Ease of use | High        | Medium            |

---

## **12. When to Use Arrays**

* When fast access is required
* When data size is known or manageable
* When order matters

---

## **13. Summary**

Arrays are the most fundamental data structure in DSA. A strong understanding of arrays helps in solving complex problems and learning advanced data structures.

Master arrays before moving to linked lists, stacks, and queues.

---

**Next Topic:** Linked List

**Author:** Money The Boss 🚀
