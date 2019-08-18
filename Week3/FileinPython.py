# File trong python
# !@author : Quang Thìn
'''
#Đọc file:
filename = "D:\Python\[AI Vietnam]\Week3\Hello.txt"
file = open(filename,mode="r",encoding="UTF-8")
data = file.read()
print(data)
#Đóng file
file.close()
file_1 = "World.txt"
file_1 = open("World.txt",mode="w",encoding="UTF-8")
text_1 = "I love python\n"
file_1.write(text_1)
text_2 = "I love AI Vietnam"
file_1.write(text_2)
file_1.close()
'''
#?---------------------------------------------------------
'''
import os

file_path1 = "Hello.txt"
check_1 = os.path.exists(file_path1)
print("File Hello.txt tồn tại không?",check_1)
file_path2 = "World.txt"
check_2 = os.path.exists(file_path2)
print("File World.txt có tồn tại không?",check_2)
'''
#*-------------------------------------------------------------
# Mở file Iris.csv
# đường dẫn file Iris.csv
filePath = "D:\Python\[AI Vietnam]\Iris.csv"
file = open(filePath,mode="r")
lines = file.readlines()
'''
# Xuất 10 hàng đầu tiên
for line in range(10):
    string = lines[line].split(',')
    print('%s ; %s ; %s ; %s ; %s ; %s' %(string[0], string[1], string[2], string[3], string[4], string[5]))
file.close()
'''
#Xuât 9 hàng đầu tiên không tính hàng đầu
for i in range(45,55):
    
    string = lines[i].split(',')
    # Các thông số của file Iris.csv
    # Vì string[0] là id nên bỏ, ta lấy từ 1 -> 4
    sepalLength = float(string[1].strip())
    sepalWidth = float(string[2].strip())
    petalLength = float(string[3].strip())
    petalWidth = float(string[4].strip())
    # 0 là Iris-setosa, 1 , 2 xem ở dưới code
    species = 0
    if string[5].strip()=="Iris-versicolor":
        species = 1
    elif string[5].strip() == "Iris-virginica":
        species = 2    
    print('%s : %s : %s : %s : %s' %(sepalLength,sepalWidth,petalLength,petalWidth,species))
file.close()
