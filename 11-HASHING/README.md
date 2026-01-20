## Hashing in Data Structures (Python)

### 1. What is Hashing?

**Hashing** is a technique used to map data to a fixed-size value (hash code) using a **hash function**. This allows **fast insertion, deletion, and searching** of data.

Real-world examples:

* Dictionaries
* Password storage
* Caches
* Database indexing

---

### 2. Hash Table

A **hash table** stores key–value pairs. A hash function converts the key into an index where the value is stored.

```
key ──> hash function ──> index ──> value
```

---

### 3. Hash Function

A good hash function:

* Is fast
* Distributes keys uniformly
* Minimizes collisions

Example:

```python
hash("apple")
```

---

### 4. Collision Handling

A **collision** occurs when two keys map to the same index.

#### 4.1 Chaining

Multiple elements are stored at the same index using a list.

#### 4.2 Open Addressing

Find another empty slot using:

* Linear Probing
* Quadratic Probing
* Double Hashing

---

### 5. Hashing in Python (Dictionary)

Python uses **hash tables internally** for dictionaries.

```python
student = {
    "name": "Rahul",
    "age": 21,
    "marks": 85
}

print(student["name"])
```

---

### 6. Common Dictionary Operations

```python
student["grade"] = "A"     # Insert
student["age"] = 22         # Update
del student["marks"]        # Delete

print("name" in student)    # Search
```

---

### 7. Time Complexity

| Operation | Average | Worst |
| --------- | ------- | ----- |
| Insert    | O(1)    | O(n)  |
| Search    | O(1)    | O(n)  |
| Delete    | O(1)    | O(n)  |

---

### 8. Hash Set

A **set** stores unique values using hashing.

```python
nums = {1, 2, 3, 4}
nums.add(5)
nums.remove(2)
```

---

### 9. Applications of Hashing

* Removing duplicates
* Frequency counting
* Two-sum problem
* Symbol tables
* Password verification

---

### 10. Common Interview Questions

* Two Sum
* First non-repeating character
* Detect duplicates
* Subarray with zero sum

---

### 11. Summary

Hashing provides **constant-time performance** for most operations and is one of the most important concepts for interviews and real-world systems.
**AUTHOR:** NITHIN KUMAR Y
