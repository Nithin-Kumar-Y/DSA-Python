## **Introduction to Arrays in Python**

### **1. What is an Array in Python?**

In Python, an **array** is a collection of elements stored in a single variable. These elements are usually of the same type and are stored in a continuous memory-like structure. In real-world Python programming, **lists** are commonly used as arrays because they are flexible, powerful, and easy to use.

Arrays are used to:

* Store multiple values efficiently
* Perform bulk operations on data
* Represent real-world collections (marks, scores, names, prices, etc.)

---

### **2. Why Use Arrays?**

* **Organized data**: Store related data together
* **Efficient processing**: Loop through multiple values easily
* **Less code**: Avoid creating many separate variables
* **Foundation for DSA**: Arrays are the base for data structures like stacks, queues, and matrices

---

### **3. Types of Arrays in Python**

Python supports arrays in two main ways:

1. **List (Most commonly used)**
2. **array module (Type-restricted arrays)**

In this guide, we focus mainly on **lists**, as they are used in almost all Python projects.

---

### **4. Creating Arrays (Lists)**

```python
numbers = [10, 20, 30, 40, 50]
names = ["Ram", "Shyam", "Arjun"]
mixed = [1, "Python", 3.14, True]
```

You can also create an empty array:

```python
arr = []
```

---

### **5. Accessing Array Elements**

Each element in an array has an index (starting from 0).

```python
numbers = [10, 20, 30, 40]
print(numbers[0])   # 10
print(numbers[-1])  # 40 (last element)
```

---

### **6. Length of an Array**

```python
numbers = [1, 2, 3, 4]
print(len(numbers))
```

---

### **7. Iterating Through Arrays**

Using a loop:

```python
for num in numbers:
    print(num)
```

Using index:

```python
for i in range(len(numbers)):
    print(numbers[i])
```

---

### **8. Adding Elements to an Array**

```python
arr = [1, 2, 3]

arr.append(4)          # Add at end
arr.insert(1, 10)      # Add at specific index
arr.extend([5, 6, 7])  # Add multiple elements
```

---

### **9. Updating Elements**

```python
arr[0] = 100
```

---

### **10. Removing Elements**

```python
arr.remove(10)   # Remove by value
arr.pop()        # Remove last element
arr.pop(1)       # Remove by index
del arr[0]       # Delete using index
```

---

### **11. Searching in Arrays**

```python
if 20 in arr:
    print(arr.index(20))
```

---

### **12. Array Slicing**

Slicing allows you to extract parts of an array.

```python
nums = [1, 2, 3, 4, 5, 6]

print(nums[:3])    # First 3 elements
print(nums[2:5])   # Middle slice
print(nums[::2])   # Step slicing
```

---

### **13. Sorting and Reversing Arrays**

```python
nums.sort()                 # Ascending order
nums.sort(reverse=True)     # Descending order
nums.reverse()              # Reverse array
```

---

### **14. List Comprehension (Powerful Feature)**

```python
squares = [x*x for x in nums]
evens = [x for x in nums if x % 2 == 0]
```

This is faster and cleaner than traditional loops.

---

### **15. Copying Arrays**

```python
copy1 = nums.copy()
copy2 = nums[:]
```

---

### **16. 2D Arrays (Matrices)**

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    print(row)
```

Used in:

* Games
* Image processing
* Mathematical computations

---

### **17. Using the array Module (Optional but Important)**

```python
from array import array

arr = array('i', [1, 2, 3, 4])
arr.append(5)
```

**Note:** All elements must be of the same type.

---

### **18. Common Mistakes**

* Index out of range
* Modifying array while looping
* Confusing copy with reference

---

### **19. Real-World Use Cases**

* Student marks list
* Cricket player scores
* Daily expenses tracker
* Sensor data collection

---

### **20. Summary**

Arrays are one of the most important concepts in Python. Mastering arrays helps you:

* Write efficient programs
* Learn Data Structures & Algorithms
* Build real-world applications

This document provides a complete foundation for arrays in Python, suitable for beginners and intermediate learners.

---

**Author:** NITHIN KUMAR Y 🚀
