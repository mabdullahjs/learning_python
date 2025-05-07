# 🧠 Understanding Memory in Python

When learning Python, you'll often hear phrases like _"create an object in memory."_ But what does **memory** actually mean?

## 🔍 What is Memory?

In Python, **memory** refers to your computer's **RAM (Random Access Memory)** — temporary storage used while your program is running.

For example:

```python
x = 10
```

This line tells Python to:
1. **Create an integer object** with the value `10`.
2. **Store that object in memory (RAM)**.
3. **Bind the variable name `x` to the memory location** of that object.

Think of `x` as a label attached to a box in RAM that holds the value `10`.

---

## ⚙️ Behind the Scenes

Let’s take another example:

```python
x = 10
y = x
```

Here's what happens:
- Python creates an object with value `10`.
- The name `x` is linked to that object in memory.
- The name `y` is also linked to the same memory location — no copy is made.

### 🧪 Check It with `id()`

```python
print(id(x))  # memory address of object 10
print(id(y))  # same address as x
```

Both `x` and `y` point to the **same object** in memory.

---

## 🧹 Python Memory Management

Python handles memory for you using:

- **Reference Counting**: tracks how many variables point to each object.
- **Garbage Collection**: automatically deletes objects no longer in use (i.e., with zero references).

---

## 🧠 Summary

- **Memory** = Temporary storage in RAM.
- Everything in Python is an **object stored in memory**.
- Variable names point to **memory addresses**, not directly to values.
- Python uses **automatic memory management** and **garbage collection**.


