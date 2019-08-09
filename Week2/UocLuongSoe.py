# C1:

import math
N = 100
e = 1
for i in range(1,N):
    e += 1/math.factorial(i)
print("Số e xấp xỉ:",e)

#C2:
E = 0
for i in range(1,1000000):
    E = (1+1/i)**i
print("Số e xấp xỉ:",E)