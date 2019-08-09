# Hàm PReLU

# @author: Quang Thin

dataset = [1,4,-6,9,-3]
alpha = 0.1
def PReLU(data,alpha):
    result = []
    for i in data:
        if i<0:
            result.append(round(alpha*int(i),3))
        else:
            result.append(i)
    return result

result = PReLU(dataset,alpha)
print(result)
