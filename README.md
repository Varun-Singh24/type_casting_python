# ==========================================
## 🔄 PYTHON TYPE CASTING EXAMPLES
# ==========================================

## 🔢 INTEGER (int)
# ------------------------------------------
print("🔢 [INTEGER CONVERSION]")
print(f"Float to Int: {int(3.14)}")       # Result: 3
print(f"String to Int: {int('10')}")      # Result: 10
print(f"Bool to Int: {int(True)}")        # Result: 1

## 🌊 FLOAT (float)
# ------------------------------------------
print("\n🌊 [FLOAT CONVERSION]")
print(f"Int to Float: {float(3)}")        # Result: 3.0
print(f"String to Float: {float('10.5')}") # Result: 10.5
print(f"Bool to Float: {float(False)}")   # Result: 0.0

## ✅ BOOLEAN (bool)
# ------------------------------------------
print("\n✅ [BOOLEAN TRUTHINESS]")
# Values that return False:
print(f"Zero: {bool(0)}")                 # ❌ False
print(f"Empty String: {bool('')}")        # ❌ False
# Values that return True:
print(f"Non-zero: {bool(-121)}")          # ✅ True
print(f"Space string: {bool(' ')}")       # ✅ True
print(f"Name string: {bool('Ashish')}")   # ✅ True

## 🛠️ NESTED CASTING (The Pro Way)
# ------------------------------------------
print("\n🛠️ [NESTED / STEP CASTING]")
# Error bypass: String -> Float -> Int
val_str = '5.99'
result = int(float(val_str)) 
print(f"Nested Casting ('5.99' -> 5): {result}")
