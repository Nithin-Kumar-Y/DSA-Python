## Greedy Algorithms

### 1. What is a Greedy Algorithm?

A **Greedy Algorithm** builds a solution step by step by always choosing the **locally optimal choice** at each step, with the hope that this leads to a globally optimal solution.

Key idea:

> Take the best choice available right now.

---

### 2. Characteristics of Greedy Algorithms

* Makes decisions one step at a time
* Never reconsiders previous choices
* Simple and fast
* Works only when the problem has the **greedy-choice property**

---

### 3. When Greedy Works

Greedy algorithms work when:

* Optimal substructure exists
* Local optimum leads to global optimum

They **do not work for all problems**.

---

### 4. Classic Greedy Problems

#### 4.1 Activity Selection Problem

Select the maximum number of activities that don't overlap.

```python
activities = [(1, 3), (2, 4), (3, 5), (0, 6), (5, 7), (8, 9)]
activities.sort(key=lambda x: x[1])

count = 1
end = activities[0][1]

for i in range(1, len(activities)):
    if activities[i][0] >= end:
        count += 1
        end = activities[i][1]

print(count)
```

---

#### 4.2 Coin Change (Greedy Version)

```python
coins = [10, 5, 2, 1]
amount = 27

result = []
for coin in coins:
    while amount >= coin:
        amount -= coin
        result.append(coin)

print(result)
```

---

#### 4.3 Fractional Knapsack

```python
items = [(60, 10), (100, 20), (120, 30)]  # (value, weight)
items.sort(key=lambda x: x[0]/x[1], reverse=True)

capacity = 50
total_value = 0

for value, weight in items:
    if capacity >= weight:
        capacity -= weight
        total_value += value
    else:
        total_value += value * (capacity / weight)
        break

print(total_value)
```

---

### 5. Greedy vs Dynamic Programming

| Greedy             | Dynamic Programming |
| ------------------ | ------------------- |
| Fast               | Slower              |
| Simple             | Complex             |
| No backtracking    | Backtracking        |
| Not always optimal | Always optimal      |

---

### 6. Time Complexity

Usually depends on sorting:

* Most greedy algorithms run in **O(n log n)**

---

### 7. Applications of Greedy Algorithms

* Scheduling problems
* Network routing
* Huffman coding
* Job sequencing
* Minimum spanning trees (Prim’s, Kruskal’s)

---

### 8. Common Interview Questions

* Activity selection
* Job sequencing with deadlines
* Minimum number of platforms
* Fractional knapsack
* Huffman encoding

---

### 9. Summary

Greedy algorithms are efficient and easy to implement, but they must be used carefully. Always verify whether the greedy-choice property holds before applying them.

**AUTHORS:** NITHIN KUAMR Y
