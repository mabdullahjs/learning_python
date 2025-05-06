
## 🧠 Python Object Types / Data Types

Python is a dynamically typed language with a rich set of built-in object types. Below is a categorized list of the most commonly used types and structures.

---

### 📌 Basic Data Types

#### 🔢 Number

Integers, Floats, Complex Numbers, Binary, Decimal, and Fractions:

```python
1234, 3.1415, 3+4j, 0b111
from decimal import Decimal
from fractions import Fraction
Decimal('1.1'), Fraction(1, 3)
```

#### 🔤 String

Standard, Byte, and Unicode strings:

```python
'spam', "Bob's", b'a\x01c', u'sp\xc4m'
```

#### ✅ Boolean

Logical values:

```python
True, False
```

#### ⛔ None

Null value:

```python
None
```

---

### 📦 Data Structures

#### 📃 List

Ordered, mutable sequences:

```python
[1, [2, 'three'], 4.5]
list(range(10))
```

#### 📦 Tuple

Ordered, immutable sequences:

```python
(1, 'spam', 4, 'U')
tuple('spam')
from collections import namedtuple
```

#### 📚 Dictionary

Key-value pairs (hash maps):

```python
{'food': 'spam', 'taste': 'yum'}
dict(hours=10)
```

#### 🔠 Set

Unordered collections of unique elements:

```python
set('abc')
{'a', 'b', 'c'}
```

---

### 📁 File Objects

For reading/writing files:

```python
open('eggs.txt')
open(r'C:\ham.bin', 'wb')
```

---

### 🧰 Others

#### ⚙️ Functions, Modules, and Classes

Python treats functions, modules, and classes as first-class objects:

```python
def func(): pass
import math
class MyClass: pass
```

---

### 🚀 Advanced Concepts

#### 🎀 Decorators

Function wrappers to add functionality:

```python
@decorator
def func(): pass
```

#### 🔁 Generators

Lazy iterables using `yield`:

```python
def gen():
    yield 1
```

#### 🔄 Iterators

Custom objects implementing `__iter__()` and `__next__()`:

```python
iter_obj = iter([1, 2, 3])
next(iter_obj)
```

#### 🧬 MetaProgramming

Code that manipulates code using `type`, metaclasses, etc.:

```python
type('MyClass', (object,), {})
```

---

## 📚 Conclusion
