## **Sorting Algorithms**

---

### **1. What is Sorting?**

**Sorting** is the process of arranging elements in a specific order, usually:

* Ascending order
* Descending order

Examples:

* Sorting marks
* Ranking players
* Ordering prices

---

### **2. Types of Sorting Algorithms**

1. Simple Sorting Algorithms
2. Efficient Sorting Algorithms

---

## **BUBBLE SORT**

### **3. Concept**

Bubble Sort repeatedly compares **adjacent elements** and swaps them if they are in the wrong order.

Largest element "bubbles" to the end in each pass.

---

### **4. Bubble Sort Code**

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = [64, 34, 25, 12, 22]
bubble_sort(arr)
print(arr)
```

---

### **5. Bubble Sort Time Complexity**

| Case    | Time  |
| ------- | ----- |
| Best    | O(n)  |
| Average | O(n²) |
| Worst   | O(n²) |

---

## **SELECTION SORT**

### **6. Concept**

Selection Sort selects the **minimum element** from unsorted part and places it at correct position.

---

### **7. Selection Sort Code**

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
```

---

### **8. Selection Sort Time Complexity**

| Case    | Time  |
| ------- | ----- |
| Best    | O(n²) |
| Average | O(n²) |
| Worst   | O(n²) |

---

## **INSERTION SORT** ⭐

### **9. Concept**

Insertion Sort builds the sorted list **one element at a time**.

Best for:

* Small datasets
* Nearly sorted arrays

---

### **10. Insertion Sort Code**

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
```

---

### **11. Insertion Sort Time Complexity**

| Case    | Time  |
| ------- | ----- |
| Best    | O(n)  |
| Average | O(n²) |
| Worst   | O(n²) |

---

## **MERGE SORT** ⭐⭐

### **12. Concept**

Merge Sort follows **Divide and Conquer** approach:

1. Divide array into halves
2. Sort each half
3. Merge sorted halves

---

### **13. Merge Sort Code**

```python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
```

---

### **14. Merge Sort Time Complexity**

| Case    | Time       |
| ------- | ---------- |
| Best    | O(n log n) |
| Average | O(n log n) |
| Worst   | O(n log n) |

---

## **QUICK SORT** ⭐⭐

### **15. Concept**

Quick Sort selects a **pivot**, partitions array, and sorts recursively.

---

### **16. Quick Sort Code**

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return left + middle + right
```

---

### **17. Quick Sort Time Complexity**

| Case    | Time       |
| ------- | ---------- |
| Best    | O(n log n) |
| Average | O(n log n) |
| Worst   | O(n²)      |

---

### **18. Comparison of Sorting Algorithms** ⭐

| Algorithm | Best       | Average    | Worst      |
| --------- | ---------- | ---------- | ---------- |
| Bubble    | O(n)       | O(n²)      | O(n²)      |
| Selection | O(n²)      | O(n²)      | O(n²)      |
| Insertion | O(n)       | O(n²)      | O(n²)      |
| Merge     | O(n log n) | O(n log n) | O(n log n) |
| Quick     | O(n log n) | O(n log n) | O(n²)      |

---

### **19. Python Built-in Sorting**

```python
arr.sort()
sorted(arr)
```

---

### **20. Common Interview Questions**

* Which sort is fastest?
* Stable vs unstable sorting
* In-place vs extra space sorting
* When to use merge sort vs quick sort

---

### **21. Summary**

Sorting algorithms are core DSA concepts used everywhere. Understanding sorting builds strong foundation for:

* Searching
* Greedy algorithms
* Dynamic programming

---

**Author:** NITHIN KUMAR Y 🚀
