import math


abc = 1

b = lambda x:math.sin(x+1)+math.cos(x**4)

print(b(abc))

y = range(-5,2)

for n in y:
    print(n,b(n))