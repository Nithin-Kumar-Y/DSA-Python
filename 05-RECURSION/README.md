## **Recursion in Python**

---

### **1. What is Recursion?**

**Recursion** is a programming technique where a function **calls itself** to solve a problem by breaking it into smaller subproblems.

In simple words:

> A function solving a problem by calling itself until a base condition is met.

---

### **2. Key Components of Recursion**

Every recursive function must have **two parts**:

1. **Base Case** – stops recursion (prevents infinite calls)
2. **Recursive Case** – function calls itself

Without a base case, recursion will cause **stack overflow**.

---

### **3. Basic Recursive Example**

```python
def hello(n):
    if n == 0:          # Base case
        return
    print("Hello")
    hello(n - 1)        # Recursive call

hello(3)
```

---

### **4. How Recursion Works (Call Stack Concept)** ⭐

Example: `factorial(4)`

```
factorial(4)
 → factorial(3)
   → factorial(2)
     → factorial(1)
       → return 1
```

Each call waits in the **call stack** until the base case returns.

---

### **5. Factorial Using Recursion**

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
```

---

### **6. Recursion vs Iteration**

| Recursion           | Iteration            |
| ------------------- | -------------------- |
| Uses function calls | Uses loops           |
| Uses stack memory   | Uses constant memory |
| Cleaner code        | Faster execution     |

---

### **7. Print Numbers Using Recursion**

#### Print 1 to N

```python
def print_1_to_n(n):
    if n == 0:
        return
    print_1_to_n(n - 1)
    print(n)
```

#### Print N to 1

```python
def print_n_to_1(n):
    if n == 0:
        return
    print(n)
    print_n_to_1(n - 1)
```

---

### **8. Sum of Numbers Using Recursion**

```python
def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)
```

---

### **9. Fibonacci Series Using Recursion** ⭐

```python
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)
```

⚠️ This solution is slow for large `n`.

---

### **10. Optimized Fibonacci (Memoization Concept)**

```python
def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]
```

---

### **11. Reverse a String Using Recursion**

```python
def reverse_string(s):
    if s == "":
        return s
    return reverse_string(s[1:]) + s[0]
```

---

### **12. Check Palindrome Using Recursion**

```python
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])
```

---

### **13. Recursion on Arrays**

```python
def array_sum(arr, n):
    if n == 0:
        return 0
    return arr[n - 1] + array_sum(arr, n - 1)
```

---

### **14. Tail Recursion (Concept)**

A function is **tail recursive** if the recursive call is the **last statement**.

```python
def fact_tail(n, result=1):
    if n == 0:
        return result
    return fact_tail(n - 1, result * n)
```

Note: Python does **not** optimize tail recursion.

---

### **15. Recursion Depth Limit**

Python default recursion limit ≈ **1000**

```python
import sys
sys.setrecursionlimit(2000)
```

---

### **16. Common Recursion Problems (Must Practice)** ⭐

* Factorial
* Fibonacci
* Power of number
* Reverse array
* Binary search
* Tower of Hanoi

---

### **17. When to Use Recursion**

* Tree & graph traversal
* Divide and conquer algorithms
* Backtracking problems

---

### **18. Common Mistakes**

* Missing base case
* Infinite recursion
* High time complexity

---

### **19. Time & Space Complexity**

* Time depends on number of calls
* Space = recursion depth (call stack)

---

### **20. Summary**

Recursion is a powerful concept that builds deep logical thinking. It is heavily used in:

* Trees
* Graphs
* Dynamic Programming

Strong recursion skills make advanced DSA topics easy.

---

**Author:** NITHIN KUMAR Y 🚀
