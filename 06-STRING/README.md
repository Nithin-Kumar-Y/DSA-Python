## **Strings in Python**

---

### **1. What is a String?**

A **string** is a sequence of characters enclosed within:

* Single quotes `' '`
* Double quotes `" "`
* Triple quotes `''' '''` or `""" """`

Strings in Python are **immutable**, meaning they **cannot be changed after creation**.

```python
s1 = 'Python'
s2 = "Programming"
s3 = '''DSA with Python'''
```

---

### **2. Why Strings are Important in DSA**

* Text processing
* Pattern matching
* Parsing input/output
* Interview problems

---

### **3. String Indexing**

```python
s = "python"
print(s[0])   # p
print(s[-1])  # n
```

Index starts from **0**.

---

### **4. String Slicing**

```python
s = "python"
print(s[0:3])   # pyt
print(s[2:])    # thon
print(s[:4])    # pyth
print(s[::-1])  # nohtyp (reverse)
```

---

### **5. String Length**

```python
len(s)
```

---

### **6. Looping Through a String**

```python
for ch in s:
    print(ch)
```

---

### **7. Common String Methods** ⭐

```python
s = "  Python Programming  "

s.lower()
s.upper()
s.strip()
s.replace("Python", "Java")
s.split()
"-".join(["a", "b", "c"])
```

---

### **8. Checking Substrings**

```python
"Py" in "Python"      # True
"Java" not in "Python"  # True
```

---

### **9. String Comparison**

```python
"abc" == "abc"   # True
"abc" < "bcd"    # True
```

Lexicographical comparison is used.

---

### **10. String Immutability** ⭐

```python
s = "hello"
# s[0] = 'H' ❌ (Error)

s = "H" + s[1:]   # Correct way
```

---

### **11. Reverse a String**

```python
s[::-1]
```

Using recursion:

```python
def reverse_string(s):
    if s == "":
        return s
    return reverse_string(s[1:]) + s[0]
```

---

### **12. Palindrome String** ⭐

```python
def is_palindrome(s):
    return s == s[::-1]
```

---

### **13. Count Characters**

```python
from collections import Counter

Counter("banana")
```

---

### **14. Remove Duplicate Characters**

```python
def remove_duplicates(s):
    return "".join(dict.fromkeys(s))
```

---

### **15. Anagram Check** ⭐

```python
def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)
```

---

### **16. String Formatting**

```python
name = "Nithin"
age = 18

f"My name is {name} and I am {age}"
```

---

### **17. String Input Problems (Interview)**

* Reverse words in a sentence
* Longest word in a string
* First non-repeating character
* Count vowels and consonants

---

### **18. Time Complexity Notes**

* Access: O(1)
* Traversal: O(n)
* Slicing: O(n)

---

### **19. Common Mistakes**

* Trying to modify string directly
* Ignoring immutability
* Inefficient concatenation in loops

---

### **20. Summary**

Strings are one of the most frequently asked topics in interviews. Mastering string manipulation builds strong fundamentals for:

* Searching algorithms
* Pattern matching
* Dynamic programming

---

**Author:** NITHIN KUMAR Y 🚀
