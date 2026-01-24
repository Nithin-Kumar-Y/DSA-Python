# 🧠 Two Pointers

This repository is a **complete, in‑depth, interview‑ready guide** to the **Two Pointers technique**.

Designed for:

* DSA beginners
* LeetCode / interview prep
* Optimizing brute‑force solutions
* Writing clean & efficient code

---

## 📌 What is the Two Pointers Technique?

Two Pointers is an algorithmic technique where **two indices (pointers)** are used to traverse a data structure (usually an array or string) **from different positions or directions**.

Instead of nested loops **O(n²)**, we reduce time to **O(n)**.

---

## 🎯 Why Use Two Pointers?

* 🚀 Improves time complexity
* 🧹 Cleaner logic than nested loops
* 💡 Core technique for interviews
* 🧠 Builds problem‑solving intuition

Used heavily in:

* Arrays
* Strings
* Linked Lists
* Sliding Window
* Binary Search variants

---

## 🔁 Types of Two Pointer Patterns

1. Opposite Direction Pointers
2. Same Direction Pointers
3. Fast & Slow Pointers
4. Window‑based Pointers
5. Partitioning Pointers

---

## 1️⃣ Opposite Direction Pointers

Pointers start from **both ends** and move toward the center.

### Example: Reverse an Array

```python
arr = [1, 2, 3, 4]
left, right = 0, len(arr) - 1

while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1
```

### Used in:

* Reverse array/string
* Palindrome check
* Pair sum (sorted array)

---

### Example: Two Sum (Sorted Array)

```python
nums = [1, 2, 4, 6, 10]
target = 8
l, r = 0, len(nums) - 1

while l < r:
    s = nums[l] + nums[r]
    if s == target:
        print(l, r)
        break
    elif s < target:
        l += 1
    else:
        r -= 1
```

---

## 2️⃣ Same Direction Pointers

Both pointers move **forward**, one faster than the other.

### Example: Remove Duplicates (Sorted Array)

```python
nums = [1, 1, 2, 2, 3]
slow = 0

for fast in range(1, len(nums)):
    if nums[fast] != nums[slow]:
        slow += 1
        nums[slow] = nums[fast]

print(nums[:slow+1])
```

---

## 3️⃣ Fast & Slow Pointers

One pointer moves faster to detect patterns.

### Example: Detect Cycle (Linked List)

```python
slow = fast = head

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
        return True
```

### Used in:

* Cycle detection
* Middle of linked list
* Happy number

---

## 4️⃣ Window‑based Two Pointers (Sliding Window)

Used when dealing with **subarrays / substrings**.

### Example: Longest Substring Without Repeating Characters

```python
s = "abcabcbb"
seen = set()
l = 0
max_len = 0

for r in range(len(s)):
    while s[r] in seen:
        seen.remove(s[l])
        l += 1
    seen.add(s[r])
    max_len = max(max_len, r - l + 1)
```

---

## 5️⃣ Partitioning Pointers

Used to **rearrange elements**.

### Example: Move Zeroes

```python
nums = [0,1,0,3,12]
slow = 0

for fast in range(len(nums)):
    if nums[fast] != 0:
        nums[slow], nums[fast] = nums[fast], nums[slow]
        slow += 1
```

---

## 🧠 How to Identify Two Pointer Problems

Ask yourself:

* Is array/string involved?
* Is it sorted or can be sorted?
* Do I need pairs/subarrays?
* Can brute force be optimized?

If yes → **Two Pointers**

---

## ⏱️ Time & Space Complexity

| Approach     | Time  | Space |
| ------------ | ----- | ----- |
| Brute Force  | O(n²) | O(1)  |
| Two Pointers | O(n)  | O(1)  |

---

## ❌ Common Mistakes

* Forgetting sorted requirement
* Infinite loops
* Pointer crossing errors
* Modifying array incorrectly

---

## 🧪 Practice Problems (Must Do)

* Two Sum II
* Valid Palindrome
* Container With Most Water
* Remove Duplicates
* Trapping Rain Water
* Move Zeroes

---

## 🔥 Two Pointers + Other Concepts

* Two Pointers + Hashing
* Two Pointers + Greedy
* Two Pointers + Sliding Window
* Two Pointers + Binary Search

---

## 🏁 Conclusion

Two Pointers is not a trick.
It is a **way of thinking**.

Master this and **half of array/string problems become easy**.

Practice → Trace pointers → Think in movement.

Happy Problem Solving 🚀

**Author:** NITHIN KUMAR Y
