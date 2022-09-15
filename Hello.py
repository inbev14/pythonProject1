import sys
print("Hello world!")
a = 100
a = b = [1, 2, 3]
print(id(a))
print(id(b))
print(sys.getrefcount(a))
print(sys.getrefcount(b))
for i in a:
    