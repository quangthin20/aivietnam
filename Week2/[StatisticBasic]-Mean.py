# @author: Quang Thin
# Thống kê cơ bản - Mean

#Lý thuyết:
import random
import numpy as np
#Hàm tạo data:
def makeData(size):
    data = []
    for i in range(size):
        data.append(random.randint(1,100))
    return data
#Hàm mean
def mean(data):
    return sum(data)/len(data)

data = makeData(10)
print(data)
print("Trung bình của data:",mean(data))

#Dùng thư viện numpy
arr = np.array([16,17,69,24,63,41,52])
print(round(arr.mean(),3))