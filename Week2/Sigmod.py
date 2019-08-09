# Định nghĩa hàm sigmod

import math

def sigmod(data):
    # Khởi tạo list rỗng
    result = [] 
    for i in data:
        # Công thức
        result.append((1/(1+math.exp(-i))))
    return result

dataset = [1,4,6,7]
result = sigmod(dataset)
print(result)