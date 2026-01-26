# 🧠 Sliding Window

This repository is a **complete, one‑shot, in‑depth guide** to the **Sliding Window technique** — one of the **most powerful patterns** in DSA.

Designed for:

* Beginners → Advanced
* LeetCode & interview preparation
* Optimizing brute‑force solutions
* Mastering array & string problems

---

## 📌 What is the Sliding Window Technique?

Sliding Window is an optimization technique used to process **contiguous subarrays or substrings** efficiently.

Instead of recalculating values for every subarray (**O(n²)**), we **slide a window** over the data in **O(n)** time.

---

## 🎯 Why Sliding Window?

* 🚀 Reduces time complexity drastically
* 🧠 Builds strong logical intuition
* 🔥 Asked heavily in interviews
* 🧹 Cleaner than nested loops

Used in:

* Strings
* Arrays
* Subarray / substring problems
* Two Pointers based problems

---

## 🪟 Types of Sliding Window Patterns

1. Fixed Size Window
2. Variable Size Window
3. Dynamic Constraint Window
4. Sliding Window + Hashing

---

## 1️⃣ Fixed Size Sliding Window

Window size **k** is constant.

### Example: Maximum Sum Subarray of Size K

```python
nums = [2, 1, 5, 1, 3, 2]
k = 3

window_sum = sum(nums[:k])
max_sum = window_sum

for i in range(k, len(nums)):
    window_sum += nums[i]
    window_sum -= nums[i-k]
    max_sum = max(max_sum, window_sum)

print(max_sum)
```

### Used in:

* Average of subarrays
* Fixed length patterns

---

## 2️⃣ Variable Size Sliding Window

Window expands and shrinks based on conditions.

### Example: Smallest Subarray with Sum ≥ Target

```python
target = 7
nums = [2,3,1,2,4,3]

left = 0
curr_sum = 0
min_len = float('inf')

for right in range(len(nums)):
    curr_sum += nums[right]
    while curr_sum >= target:
        min_len = min(min_len, right - left + 1)
        curr_sum -= nums[left]
        left += 1

print(min_len if min_len != float('inf') else 0)
```

---

## 3️⃣ Sliding Window + Hashing

Used when **frequency / uniqueness** matters.

### Example: Longest Substring Without Repeating Characters

```python
s = "abcabcbb"
seen = set()
left = 0
max_len = 0

for right in range(len(s)):
    while s[right] in seen:
        seen.remove(s[left])
        left += 1
    seen.add(s[right])
    max_len = max(max_len, right - left + 1)

print(max_len)
```

---

## 4️⃣ Sliding Window with Frequency Map

### Example: Longest Repeating Character Replacement

```python
from collections import defaultdict

s = "AABABBA"
k = 1
count = defaultdict(int)
left = 0
max_count = 0
result = 0

for right in range(len(s)):
    count[s[right]] += 1
    max_count = max(max_count, count[s[right]])

    while (right - left + 1) - max_count > k:
        count[s[left]] -= 1
        left += 1

    result = max(result, right - left + 1)

print(result)
```

---

## 🧠 How to Identify Sliding Window Problems

Ask these questions:

* Is it subarray or substring?
* Is contiguity required?
* Can brute force be optimized?
* Is there a growing/shrinking condition?

If yes → **Sliding Window**

---

## ❌ Common Mistakes

* Forgetting to shrink window
* Wrong condition in `while`
* Off‑by‑one errors
* Resetting window unnecessarily

---

## ⏱️ Time & Space Complexity

| Approach       | Time  | Space       |
| -------------- | ----- | ----------- |
| Brute Force    | O(n²) | O(1)        |
| Sliding Window | O(n)  | O(1) / O(k) |

---

## 🧪 Must‑Do Practice Problems

* Maximum Sum Subarray
* Longest Substring Without Repeating Characters
* Minimum Window Substring
* Permutation in String
* Fruits Into Baskets
* Subarray Product Less Than K

---

## 🔥 Sliding Window vs Two Pointers

Sliding Window **is a specialized form of Two Pointers** where:

* Window is always contiguous
* One pointer expands
* One pointer shrinks

---

## 🏁 Conclusion

Sliding Window is not optional — it is **mandatory for interviews**.

Once mastered, it turns complex problems into simple loops.

Practice → Trace window → Think constraints.

Happy Coding 🚀

**Author:** NITHIN KUMAR Y
