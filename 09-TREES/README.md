## Trees in Data Structures (Python)

### 1. What is a Tree?

A **tree** is a non-linear data structure that represents data in a **hierarchical** form. It consists of nodes connected by edges, with a single **root node** at the top.

Real-world examples:

* Family tree
* Folder structure in OS
* Organization hierarchy

---

### 2. Basic Terminology

* **Node**: An element in the tree
* **Root**: Topmost node
* **Parent / Child**: Relationship between nodes
* **Leaf**: Node with no children
* **Edge**: Connection between nodes
* **Height**: Longest path from root to leaf
* **Depth**: Distance from root to a node

---

### 3. Types of Trees

* General Tree
* Binary Tree
* Binary Search Tree (BST)
* Balanced Tree
* Heap
* Trie

---

### 4. Binary Tree

A tree where each node has **at most two children** (left and right).

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
```

---

### 5. Tree Traversals

#### Inorder (Left → Root → Right)

```python
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=' ')
        inorder(root.right)
```

#### Preorder (Root → Left → Right)

```python
def preorder(root):
    if root:
        print(root.data, end=' ')
        preorder(root.left)
        preorder(root.right)
```

#### Postorder (Left → Right → Root)

```python
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=' ')
```

---

### 6. Binary Search Tree (BST)

A BST follows the rule:

* Left subtree < Root
* Right subtree > Root

```python
def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root
```

---

### 7. Searching in BST

```python
def search(root, key):
    if root is None or root.data == key:
        return root
    if key < root.data:
        return search(root.left, key)
    return search(root.right, key)
```

---

### 8. Time Complexity

| Operation | BST (Avg) | BST (Worst) |
| --------- | --------- | ----------- |
| Search    | O(log n)  | O(n)        |
| Insert    | O(log n)  | O(n)        |
| Delete    | O(log n)  | O(n)        |

---

### 9. Applications of Trees

* Databases (Indexing)
* File systems
* Compilers (syntax trees)
* Search engines
* AI & ML

---

### 10. Common Interview Questions

* Height of a tree
* Diameter of a tree
* Lowest Common Ancestor (LCA)
* Check if tree is balanced
* Mirror of a tree

---

### 11. Summary

Trees are powerful data structures used to represent hierarchical data efficiently. Binary Trees and BSTs are fundamental for interviews and advanced algorithms.

**AUTHOR:** NITHIN KUMAR Y
