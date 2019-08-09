# Ước lượng số PI
import random
import math
N = 1000000

N_T = 0
for i in range(N):
    # Sinh ra tọa độ x,y thuộc đường tròn bán kính r=1
    x = 2*random.random()-1
    y = 2*random.random()-1
    if (math.sqrt(x**2+y**2<=1)):
        N_T +=1
print("Số Pi xấp xỉ:",4*N_T/N)
