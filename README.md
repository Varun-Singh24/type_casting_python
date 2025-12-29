# 🔄 TYPE CASTING IN PYTHON 🔄

# 🔢 1. Integer Conversion (int)
# Converting floating points, numeric strings, and booleans
print("🔢 ----- INTEGER -----")
print(int(3.14))       # 💡 Drops decimals (3)
print(int('10'))       # 💡 String to whole number (10)
print(int(False))      # 💡 False maps to 0
print(int(True))       # 💡 True maps to 1

# 🌊 2. Float Conversion (float)
# Adding precision to integers and strings
print("\n🌊 ----- FLOAT -----")
print(float(3))        # 💡 Adds decimal (3.0)
print(float('10'))     # 💡 String to float (10.0)
print(float('10.5'))   # 💡 Decimal string to float (10.5)
print(float(True))     # 💡 True maps to 1.0

# ✅ 3. Boolean Conversion (bool)
# Truthiness check: 0 and Empty values are False, others are True
print("\n✅ ----- BOOLEAN -----") 
print(bool(1))            # True
print(bool(1000))         # True
print(bool(-12221))       # True (Negative numbers are still True)
print(bool(0))            # ❌ False
print(bool(0.0))          # ❌ False
print(bool("Ashish"))     # True
print(bool(' '))          # True (Space counts as content)
print(bool(''))           # ❌ False (Empty string)

# ⚠️ 4. Exceptions & Nested Casting
print("\n⚠️ ----- EXCEPTIONS -----")
# ❌ print(int('3.14'))   # ERROR: Cannot go direct from decimal string to int

# ✅ The "Two-Step" Solution:
# String ('5.99') -> Float (5.99) -> Int (5)
print(int(float('5.99'))) 

# Float (8.14) -> Int (8) -> Float (8.0)
print(float(int(8.14)))
