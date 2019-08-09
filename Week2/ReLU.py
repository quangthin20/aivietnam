# Hàm ReLU

# @author: Quang Thin

dataset = [1,4,-6,9,3]
def ReLU(data):
    result = []
    for i in data:
        if i<0:
            result.append(0)
        else:
            result.append(i)
    return result

result = ReLU(dataset)
print(result)