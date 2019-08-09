
# KHÓA HỌC AI VIETNAM - Weed1
![Facebook](http://imobizone.com/wp-content/uploads/2013/03/Facebook-for-Android-i-mobile-IQ6-1.png)
[Facebook](https://www.facebook.com/PGS.TienSi.QuangThin)

## Lý thuyêt
### A. Hàm xây dựng sẵn trong Python – math và random
#### I. Math module
>Math module trong python chứa các hàm về những toán học phổ biến như lượng giác, logarith, hay hàm lũy thừa. Trong bài này, chúng ta sẽ tìm hiểu qua những hàm và hằng số phổ biến trong module `math`.

>Để dùng module math, trước tiên chúng ta cần khai báo hay gọi nó ra bằng dòng code import math. Để gọi hàm từ module math, chúng ta dùng cú pháp math.ten_ham(), trong đó ten_ham() là một hàm số trong module math. Để dùng hằng số, chúng ta dùng cú pháp math.ten_hang_so, trong đó ten_hang_so là một hằng số.

>Để biết trong module này có những hàm nào, chúng ta cần đọc tài liệu mô tả về module đó. Link https://docs.python.org/3/library/math.html mô tả chi tiết các hàm và cách sử dụng trong module math. Ở đây, chúng ta chỉ tìm hiểu qua những hàm quan trọng và phổ biến. Chúng ta học lướt qua để biết nó có tồn tại, chứ không cần phải nhớ. Khi code thực tế, chúng ta có thể tham khảo lại hoặc tìm kiếm google một cách dễ dàng.

>Sau đây là một số hàm phổ biến trong module math.
1. Hàm `math.fabs(x)`: trả về giá trị tuyệt đố i(số thực)của x
Ví dụ:
```python
import math
a = -20
b = 6
# c là giá trị tuyệt đối của a
c = math.fabs(a)
print("c = ",c)
# d là giá trị tuyệt đối của b
d = math.fabs(b)
print("d = ",d)
```
Kết quả sau khi chạy:
```python
c = 20.0
d = 6.0
```
2. Hàm `math.exp(x)`: trả về giá trị $$e^{x}$$
``` python
import math
x = 2
print(math.exp(x))
```
Kết quả sau khi chạy:
```python
7.38905609893065
```
3. Hàm `math.log(x)`: Trả về giá trị logarith của x với cơ số e.
```python
import math

x = 4
print(math.log(x))
print(math.log(math.e)
```
Kết quả:
```python
1.3862943611198906
1.0
```
4. Hàm `math.sqrt(x)`: Trả về giá trị căn bậc 2 của x
```python
import math

x = 4
print(math.sqrt(x))
```
Kết quả:
```python
2.0
```
>Ngoài ra, ta có thể tham khảo thêm tại: https://docs.python.org/3/library/math.html

#### II. Random Module
1. Hàm ```random.random()``` trả về giá trị ngẫu nhiên trong nửa khoảng [0;1)
```python
import random

print(random.random())
print(random.random())
print(random.random())
print(random.random())
```
Kết quả:
```python
0.9935084951991164
0.5192882043733612
0.31020267547711977
0.3710197566814225
```
2. Hàm `random.randint(a, b)`: Trả về một giá trị ngẫu nhiên kiểu int trong đoạn [a, b].
```python
import random

print(random.randint(1,9))
print(random.randint(1,9))
print(random.randint(1,9))
print(random.randint(1,9))
```
Kết quả:
```python
3
8
3
5
```
>Phần đọc thêm: đọc thêm về module random tại https://docs.python.org/3/library/random.html

### B. Tìm hiểu về hàm:
 **1. Định nghĩa:** Hàm là một chuỗi các bước (câu lệnh) liên quan tạo nên một nhiệm vụ lớn hơn, thường được gọi từ nhiều nơi trong một chương trình.

**2 . Cách khai báo hàm**
```python
def <tên_hàm> (<tham_số_tùy_chọn>):
	<khối_lệnh> #Phần viết hàm
```
Ví dụ: Định nghĩa hàm diện tích hình chữ nhật với hai tham số width, height
```python
# định nghĩa hàm
def dientichHCN(width,height):
	return width*height
print(dientichHCN(20,10))
```
Kết quả là:
```python
200
```
 **3. Ghi nhớ về Hàm:**  
– Tên hàm nên bắt đầu bằng kí tự viết thường  
– Tên hàm bao gồm kí tự, số và dấu gạch dưới  
– Dấu đóng mở ngoặc `()` đi sau tên hàm  
– Dấu hai chấm `:` đi sau dấu đóng mở ngoặc `()`  
– Luôn thụt lề khi thực hiện phần code thân hàm
**4. Tham số của hàm**
>**Định nghĩa:** Tham số của hàm là một biến (được định nghĩa trong dấu mở ngoặc ở câu lệnh `def`) đóng vai trò là giá trị đầu vào cho một hàm.

Ví dụ:
```python
def sayHello(name):
	print("Hello"+name)
sayHello("Jacky")
```
Kết quả:
```python
Hello Jacky
```
**5.  Hàm trả về giá trị với từ khóa  **return****
Ví dụ:
```python
# hàm có mục đích cộng giá trị của biến tham số thêm 3
def add_three(value):
    result = value + 3

    # trả kết quả về
    return result

# gọi hàm và lưu kết quả vào biến sum1
sum1 = add_three(4)

# gọi hàm và lưu kết quả vào biến sum2
sum2 = add_three(8)

print('Kết quả của cộng 4 với 3 là:', sum1)
print('Kết quả của cộng 8 với 3 là:', sum2)
```
Kết quả:
```
Kết quả của cộng 4 với 3 là: 7
Kết quả của cộng 8 với 3 là: 11
```
### C. Điều kiện if-else
#### I. Phép so sánh logic

Python hỗ trợ các phép so sánh cơ bản giữa hai biến. Ví dụ chúng ta có thể tìm ra quan hệ lớn hơn, nhỏ hơn, hay khác nhau giữa hai biến số. Bảng sau mô tả các phép so sánh giữa hai biến.

![](https://aivietnam.ai/wp-content/uploads/2019/07/condition1.png)

Ví dụ cho hai biến  `a`  và  `b`  kiểu  `int`, chúng ta có thể so sánh hai biến như sau

![](https://aivietnam.ai/wp-content/uploads/2019/07/chap2_condition_2.png)

Các phép so sánh trả về giá trị  `True`  hoặc  `False`, nên khi đọc code, chúng ta nên đặt câu hỏi để dễ hình dung ý nghĩa hơn. Thực thi đoạn code trên ta được
#### II. Điều kiện if

Trong pyhon, một khối code (một hay nhiều dòng code) có thể được thực thi khi một điều kiện nào đó được thỏa mãn. Điều kiện  `if`  cho phép chúng ta ràng buộc ngữ cảnh để thực thi một khối code. Điều kiện  `if`  trong python có cú pháp như sau

![](https://aivietnam.ai/wp-content/uploads/2019/07/condition77.png)

Ở đây,  `condition`  có thể là một biểu thức so sánh phức tạp, nhưng giá trị của  `condition`  là  `True`  hoặc  `False`.

Nếu  `condition`  có giá trị là  `True`  thì khối code bên trong  `if`  được thực thi. Nếu  `condition`  có giá trị là  `False`  thì khối code trong  `if`  được bỏ qua (không thực thi) và chương trình tiếp tục với  `khối code k2`. Lưu ý là sau  `condition`  yêu cầu dấu 2 chấm  `:`  và khối code bên trong  `if`  phải thụt lề phù hợp.
