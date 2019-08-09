# Hàm Tanh
# @authour QuangThin
import math

dataset = [1,5,-4,3,-2]
def tanhFunction(data):
    result = []
    for i in data:
        result.append((2/(1+math.exp(-2*i)))-1)
    return result

result = tanhFunction(dataset)
print(result)