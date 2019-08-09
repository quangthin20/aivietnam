''' Dùng vòng lặp while - break :lặp lại việc sinh ra một số nguyên, 
ngẫu nhiên nằm trong đoạn [0, 10]. Vòng lặp dừng lại khi số ngẫu nhiên sinh ra là số 5.'''
import random

while True:
    num = random.randint(1,10)
    print("Số sinh ra có giá trị là:",num)
    if num==5:
        break
print("Chương trình kết thúc.")
