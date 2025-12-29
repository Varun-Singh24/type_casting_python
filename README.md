## 🔄 Type Casting & Data Conversion in Python

### This repository explores the mechanics of **Type Conversion** in Python, demonstrating how to transform data between Integers, Floats, and Booleans.

---

## 🛠️ Tools & Environment

* **Language:** Python 🐍
* **Environment:** Jupyter Notebook / VS Code
* **Concepts Used:** - Data Type Identification
* Explicit Type Conversion
* Boolean Truthiness Logic
* Error Handling (Nested Casting)


---

## 🔢 Integer Conversion (`int`)

### 📌 Concept

The `int()` function converts a value into a whole number. It does not round; it simply **truncates** (chops off) the decimal part.

### 🧾 Code

```python
print(int(3.14))    # Result: 3 (Truncates decimal)
print(int('10'))    # Result: 10 (String to Int)
print(int(False))   # Result: 0 (Boolean False is 0)
print(int(True))    # Result: 1 (Boolean True is 1)

```

### 📘 Explanation

* **Floating points:** Only the part before the dot is kept.
* **Booleans:** Python treats `True` as 1 and `False` as 0.

---

## 🌊 Float Conversion (`float`)

### 📌 Concept

The `float()` function converts integers or numeric strings into floating-point numbers (numbers with decimals).

### 🧾 Code

```python
print(float(3))       # Result: 3.0
print(float('10'))    # Result: 10.0
print(float('10.5'))  # Result: 10.5
print(float(True))    # Result: 1.0

```

### 🎯 Use Case

✔ Ensuring precision in division.
✔ Converting price data from strings to numbers for calculations.

---

## ✅ Boolean "Truthiness" (`bool`)

### 📌 Concept

The `bool()` function checks if a value evaluates to **True** or **False**. This is the foundation of conditional logic.

### 🧾 Code

```python
print(bool(1))            # True
print(bool(0))            # False (Zero is always False)
print(bool("Ashish"))     # True (Non-empty strings are True)
print(bool(''))           # False (Empty string is False)
print(bool(' '))          # True (Space is a character!)

```

### 📘 Explanation

* **False values:** `0`, `0.0`, `None`, and empty collections (`''`, `[]`, `{}`).
* **True values:** Everything else.

---

## 🛠️ Advanced: Nested Casting & Exceptions

### 📌 Concept

Python cannot directly convert a string with a decimal (like `"3.14"`) into an integer. You must use a "two-step" process.

### 🧾 Code

```python
print(int('3.14'))      # ❌ This would throw a ValueError

# ✅ Correct Approach (Nested Casting)
# Step 1: String to Float -> Step 2: Float to Int
print(int(float('5.99')))  # Result: 5

# Step 1: Float to Int -> Step 2: Int back to Float
print(float(int(8.14)))    # Result: 8.0

```

### 🎯 Use Case

✔ Cleaning "dirty" data from CSV files where numbers might be stored as strings with decimals.

---

## 🧠 Concepts Practiced

* **Explicit Casting:** Manually changing types.
* **Truncation vs. Rounding:** Understanding how `int()` behaves.
* **Boolean Logic:** Mastering empty vs. non-empty values.
* **Error Prevention:** Handling complex string-to-number conversions.

---

⭐ If you find this helpful, consider starring the repository! 🚀

