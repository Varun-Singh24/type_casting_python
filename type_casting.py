# Type Casting 

# int 
print(3.14)
print(int('10'))
print(int(False))
print(int(True))

# float 
print("-----FLOAT-----")
print(float(3))
print(float('10'))
print(float('10.5'))
print(float(True))

# Bool 
print("---------bool-----------") 
print(bool(1)) 
print(bool(1000)) 
print(bool(-12221)) 
print(bool(0)) 
print(bool(0.0)) 
print(bool(2562455.63)) 
print(bool("Ashish Singh"))
print(bool('A'))
print(bool(' '))  # A single Space -- True
print(bool(''))   # no space -- False 
print(bool)

#  Exceptions 
# print(int('3.14'))  # Error -- two step procees 
print(int(float('5.99')))  # correct 

print(float(int(8.14)))