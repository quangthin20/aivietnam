# Hàm SoftPlus

# @author: Quang Thin Tran
import math

dataset = [1,4,-6,9,-3]
def SoftPlus(data):
    result = []
    for x in data:
        result.append(math.log(1+math.exp(x)))
    return result

result = SoftPlus(dataset)
print(result)
