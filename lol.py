from math import *
a = 0.5543
f = round(a, 1)
b = modf(f)
c = b[0]
d = b[1]
print(type(c))
print(type(d))
print(c)
print(d)
print(f)
