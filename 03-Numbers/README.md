Here's a **detailed breakdown of numbers in Python**, including:

* Numeric types
* Operators
* Comparison
* Random numbers
* Fractions
* Sets

Wrapped in a single `README.md` code block for GitHub.

---

````markdown
# 🔢 Numbers in Python — A Complete Guide

Python provides rich support for working with numbers. This includes:

- 📚 Numeric Types
- ➕ Arithmetic & Assignment Operators
- 🔍 Comparison Operators
- 🎲 Random Numbers
- 🧮 Fractions
- 🧺 Sets

---

## 📚 Numeric Types in Python

```python
# Integer
a = 5

# Float
b = 3.14

# Complex
c = 2 + 3j

# Type check
print(type(a))  # <class 'int'>
print(type(b))  # <class 'float'>
print(type(c))  # <class 'complex'>
```

---

## ➕ Arithmetic Operators

```python
x = 10
y = 3

print(x + y)  # Addition => 13
print(x - y)  # Subtraction => 7
print(x * y)  # Multiplication => 30
print(x / y)  # Division => 3.333...
print(x // y) # Floor division => 3
print(x % y)  # Modulus => 1
print(x ** y) # Exponentiation => 1000
```

---

## 📝 Assignment Operators

```python
x = 5
x += 2  # x = x + 2
x -= 1  # x = x - 1
x *= 3  # x = x * 3
x /= 2  # x = x / 2
```

---

## 🔍 Comparison Operators

```python
a = 10
b = 20

print(a == b)  # False
print(a != b)  # True
print(a < b)   # True
print(a > b)   # False
print(a <= b)  # True
print(a >= b)  # False
```

---

## 🎲 Random Numbers

```python
import random

print(random.randint(1, 10))     # Random int from 1 to 10
print(random.random())           # Random float from 0 to 1
print(random.uniform(1, 5))      # Random float from 1 to 5
print(random.choice([1, 2, 3]))  # Random element from list
```

---

## 🧮 Fractions (Exact Arithmetic)

```python
from fractions import Fraction

f1 = Fraction(1, 3)
f2 = Fraction(2, 5)
result = f1 + f2

print(result)         # 11/15
print(float(result))  # 0.733...
```

---

## 🧺 Sets (Unique Unordered Values)

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)  # Union => {1, 2, 3, 4, 5}
print(a & b)  # Intersection => {3}
print(a - b)  # Difference => {1, 2}
print(a ^ b)  # Symmetric Difference => {1, 2, 4, 5}
```

- Sets automatically remove duplicates:
  ```python
  set([1, 2, 2, 3])  # => {1, 2, 3}
  ```

---

## ✅ Summary

| Category         | Usage Example        |
|------------------|----------------------|
| Numeric Types     | `int`, `float`, `complex` |
| Arithmetic        | `+`, `-`, `*`, `/`, `**`, `%` |
| Comparison        | `==`, `!=`, `>`, `<`, `>=`, `<=` |
| Random Module     | `random.randint()`, `random.random()` |
| Fractions Module  | `Fraction(1, 3)` |
| Sets              | `{1, 2, 3}`, `set()` with set operations |

---

Python makes working with numbers powerful and readable — from simple math to probability and algebra!

````
