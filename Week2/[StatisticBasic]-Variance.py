# Thống kê cơ bản - Variance - phương sai
#! @author: Quang Thìn
import random
import math
# Tạo Data
def makeData(size):
    data = []
    for i in range(size):
        data.append(random.randint(1,100))
    return data
# Hàm mean
def mean(data):
    return sum(data)/len(data)
# Hàm variance
def variance(data):
    Mean = mean(data)
    #? diff là list chứa giá trị x-mean của data 
    diff = []
    for x in data:
        diff.append(x-Mean)
    squared_diff = []
    for num in diff:
        squared_diff.append(num**2)
    return sum(squared_diff)/len(data)

data = makeData(20)
print(data)
print("Phương sai của dữ liệu:",variance(data))
print("Độ lệch chuẩn của dữ liệu",math.sqrt(variance(data)))
    