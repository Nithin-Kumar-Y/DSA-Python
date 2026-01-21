## Dynamic Programming (DP)

### 1. What is Dynamic Programming?

**Dynamic Programming (DP)** is an algorithmic technique used to solve problems by **breaking them into overlapping subproblems**, solving each subproblem once, and **storing the results** to avoid repeated computation.

In simple words:

> Solve once, reuse many times.

---

### 2. When to Use Dynamic Programming

A problem is suitable for DP if it has:

1. **Overlapping Subproblems**
2. **Optimal Substructure** (optimal solution can be built from optimal solutions of subproblems)

---

### 3. Approaches in Dynamic Programming

#### 3.1 Memoization (Top-Down)

* Uses recursion
* Stores results in cache

```python
def fib(n, dp):
    if n <= 1:
        return n
    if dp[n] != -1:
        return dp[n]
    dp[n] = fib(n-1, dp) + fib(n-2, dp)
    return dp[n]

n = 6
dp = [-1] * (n + 1)
print(fib(n, dp))
```

---

#### 3.2 Tabulation (Bottom-Up)

* Uses iteration
* No recursion

```python
def fib(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

print(fib(6))
```

---

### 4. Classic DP Problems

#### 4.1 Fibonacci Series

(Time: O(n), Space: O(n))

---

#### 4.2 0/1 Knapsack

```python
def knapsack(wt, val, W, n):
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if wt[i-1] <= w:
                dp[i][w] = max(val[i-1] + dp[i-1][w-wt[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][W]
```

---

#### 4.3 Longest Common Subsequence (LCS)

```python
def lcs(X, Y):
    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i-1] == Y[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]
```

---

#### 4.4 Longest Increasing Subsequence (LIS)

```python
def lis(nums):
    n = len(nums)
    dp = [1] * n

    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
```

---

### 5. Greedy vs Dynamic Programming

| Greedy             | Dynamic Programming |
| ------------------ | ------------------- |
| Local optimum      | Global optimum      |
| Fast               | Slower              |
| Simple             | Complex             |
| Not always correct | Always correct      |

---

### 6. Common Mistakes in DP

* Missing base cases
* Wrong state definition
* Incorrect transitions
* High space usage

---

### 7. Interview Tips for DP

* Identify states clearly
* Write recurrence relation
* Decide memoization or tabulation
* Optimize space if possible

---

### 8. Applications of Dynamic Programming

* Resource optimization
* String matching
* Path finding problems
* Bioinformatics
* Financial planning

---

### 9. Summary

Dynamic Programming is one of the most important and powerful techniques in computer science. Mastering DP significantly increases your problem-solving and interview success.

**AUTHORS:** NITHIN KUMAR Y
