# Bài tập:
'''
Cho list data = [1, 2, 3, 4, 5, 6, 7, 8, 9]. Các giá trị trong list thể hiện điểm số của mỗi phần tử.
Phần tử đầu có điểm số nhỏ nhất là 1 và phần tử cuối có điểm số lớn nhất là 9.
Yêu cầu đặt ra là chọn ngẫu nhiên 1000 phần tử từ list data, 
và phần tử có điểm số lớn hơn nên được chọn nhiều hơn. 
Các bạn hãy suy nghĩ và cài đặt chương trình thỏa mãn yêu cầu trên bằng nhiều cách nhất có thể.
'''
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
import random
for i in range(20):
    x = random.randint(1,9)
    print(x)













































'''
count1 = count2 = count3 = count4 = count5 = count6 = count7 = count8 = count9 = 0
for i in range(1000):
    x = random.random()
    if x > 9/45:
        count9 +=1
    elif x > 8/45:
        count8+=1
    elif x > 7/45:
        count7+=1
    elif x > 6/45:
        count6+=1
    elif x > 5/45:
        count5+=1
    elif x > 4/45:
        count4+=1
    elif x > 5/45:
        count5+=1
    elif x > 4/45:
        count4+=1
    elif x > 3/45:
        count3+=1
    elif x > 2/45:
        count2+=1
    else:
        count1+=1
print("Số 1 xuất hiện:",count1)
print("Số 2 xuất hiện:",count2)
print("Số 3 xuất hiện:",count3)
print("Số 4 xuất hiện:",count4)
print("Số 5 xuất hiện:",count5)
print("Số 6 xuất hiện:",count6)
print("Số 7 xuất hiện:",count7)
print("Số 8 xuất hiện:",count8)
print("Số 9 xuất hiện:",count9)
'''
   