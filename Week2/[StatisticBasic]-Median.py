# @author: Quang Thin
# Thống kê cơ bản - Median : Trung vị

#Lý thuyết:
import random
import numpy as np
#Hàm tạo data:
def makeData(size):
    data = []
    for i in range(size):
        data.append(random.randint(1,100))
    return sorted(data)
#Hàm median
def median(data):
    size = len(data)
    if size%2==1:
        return data[size//2]
    else:
        temp = size//2
        return (data[temp-1]+data[temp])/2
data = makeData(9)
print(data)
print("Trung vị của data:",median(data))

#Dùng thư viện numpy
arr = np.array([16,17,69,24,63,41,52,41])
result = median(arr)
print(result)
