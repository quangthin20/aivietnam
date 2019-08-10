# @author: Quang Thin
# Thống kê cơ bản - Mode

#Lý thuyết:
import random
from collections import Counter
import numpy as np
#Hàm tạo data:
def makeData(size):
    data = []
    for i in range(size):
        data.append(random.randint(1,50))
    return data
#Hàm mode

#Trường hợp 1: Có 1 mode
def mode(data):
    c = Counter(data)
    mode = c.most_common(1)
    return mode[0][0]
data = makeData(50)
print(data)
print("Mode của data:",mode(data))
#Trường hợp 2: Có nhiều mode
dataset = [10,12,11,14,10,12,14,11,10,12,14,15]
def Mode(data):
    mode = []
    c = Counter(data)
    num_freq = c.most_common()
    # Kết quả: num_freq = [(10,3);(12,3);(14,3);(11,2);(15,1)]
    maxcount = num_freq[0][1]
    for num in num_freq:
        if num[1]==maxcount:
            mode.append(num[0])
    return mode
print(Mode(dataset))
#Sử dụng numpy 
data_set = np.array([10,12,11,14,10,12,14,11,10,12,14,15])
result = mode(data_set)
print(result)