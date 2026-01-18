## **Searching Algorithms**

---

### **1. What is Searching?**

**Searching** is the process of finding the position of a given element (key) in a data structure such as an array, list, or string.

Example:

* Finding a student roll number
* Searching a name in a contact list
* Finding a value in sorted data

---

### **2. Types of Searching Algorithms**

1. **Linear Search**
2. **Binary Search**

---

## **LINEAR SEARCH**

### **3. What is Linear Search?**

Linear search checks **each element one by one** until the key is found or the list ends.

Used when:

* Data is **unsorted**
* Small datasets

---

### **4. Linear Search Algorithm**

Steps:

1. Start from first element
2. Compare each element with key
3. Stop when found or list ends

---

### **5. Linear Search Code (Python)**

```python
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

arr = [10, 20, 30, 40, 50]
print(linear_search(arr, 30))
```

---

### **6. Linear Search Time Complexity**

| Case    | Time |
| ------- | ---- |
| Best    | O(1) |
| Average | O(n) |
| Worst   | O(n) |

---

### **7. Advantages & Disadvantages**

**Advantages**:

* Simple to implement
* Works on unsorted data

**Disadvantages**:

* Slow for large datasets

---

## **BINARY SEARCH** ⭐

### **8. What is Binary Search?**

Binary search works by **dividing the search space into half** repeatedly.

⚠️ **Condition:** Data must be **sorted**.

---

### **9. Binary Search Algorithm**

Steps:

1. Find middle element
2. Compare with key
3. If key < mid → search left
4. If key > mid → search right
5. Repeat until found or range ends

---

### **10. Binary Search (Iterative)**

```python
def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = [10, 20, 30, 40, 50]
print(binary_search(arr, 40))
```

---

### **11. Binary Search (Recursive)**

```python
def binary_search_rec(arr, low, high, key):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == key:
        return mid
    elif arr[mid] < key:
        return binary_search_rec(arr, mid + 1, high, key)
    else:
        return binary_search_rec(arr, low, mid - 1, key)
```

---

### **12. Binary Search Time Complexity**

| Case    | Time     |
| ------- | -------- |
| Best    | O(1)     |
| Average | O(log n) |
| Worst   | O(log n) |

---

### **13. Linear vs Binary Search** ⭐

| Feature    | Linear     | Binary           |
| ---------- | ---------- | ---------------- |
| Data Order | Any        | Sorted only      |
| Speed      | Slow       | Fast             |
| Technique  | Sequential | Divide & conquer |

---

### **14. Searching in Strings**

```python
s = "python"
key = 't'

for i in range(len(s)):
    if s[i] == key:
        print(i)
```

---

### **15. Built-in Searching in Python**

```python
arr.index(30)     # List
"py" in "python"  # String
```

---

### **16. Common Interview Problems** ⭐

* First occurrence of element
* Last occurrence of element
* Count occurrences
* Search in rotated sorted array
* Binary search on answer

---

### **17. Common Mistakes**

* Using binary search on unsorted data
* Wrong mid calculation
* Infinite loop

---

### **18. Applications of Searching**

* Databases
* Search engines
* OS scheduling
* AI & ML lookups

---

### **19. Summary**

Searching algorithms help locate data efficiently. Linear search is simple but slow, while binary search is fast but requires sorted data. These algorithms are foundations for advanced techniques.

---

**Author:** NITHIN KUMAR Y 🚀
