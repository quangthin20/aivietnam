
# KHÓA HỌC AI VIETNAM - Week2
[Facebook](https://www.facebook.com/PGS.TienSi.QuangThin)

## A. Lý thuyêt
### I. Vòng lặp for và while
#### 1. Vòng lặp for
Vòng lặp for trong Python cho phép chúng ta thực thi một khối code nhiều lần hay duyệt các phần tử một iterable. Cú pháp của vòng lặp for như sau:

![](https://aivietnam.ai/wp-content/uploads/2019/07/for1.png)

trong đó iterable có thể là list, range, hay file.

Ví dụ: 
```python
N = 5
for i in range(N):
    print(i)
```
Kết quả:
```python
0
1
2
3
4
```
Chúng ta có thể sử dụng từ khóa `break` để thoát khỏi vòng lặp `for`. Từ khóa break thường được dùng kết hợp với điều kiện `if`.Ví dụ: 
```python
N = 5
for i in range(N):
    print(i)
    if n>2:
        break
```
Kết quả:
```python
0
1
2
```
Một từ khóa khác cũng được dùng phổ biến trong các vòng lặp là từ khóa `continue`. Khi đang thực thi khối code k trong vòng lặp for và gặp từ khóa này, chương trình sẽ không thực thi phần code còn lại (phần code chưa thực thi) của k mà quay lại phần biểu thức for. Vi dụ sau duyệt các phần tử trong một iterable và khi phần tử có giá trị là 2, từ khóa `continue` sẽ được gọi.
```python
N = 5
for i in range(N):
    print(i)
    if n>2:
        continue
```
Kết quả:
```python
0
1
3
4
```
#### 2. Vòng lặp while
Vòng lặp while có cú pháp như sau
![](https://aivietnam.ai/wp-content/uploads/2019/07/chap2_while_1-768x562.png)
```python
N = 5
i = 0
while (i<N):
    print(i)
    i+=1
```
Kết quả:
```python
0
1
2
3
4
```
### II. Ước lượng số PI và e
#### 1. Ước lượng số PI:
Chúng ta sẽ cài đặt chương trình để ước lượng số PI dùng các số ngẫu nhiên có phân bố đều (uniform distribution). Các bước cài đặt chương trình như sau:

1. Cho trước hình vuông V có cạnh s = 2 và hình tròn T có bán kính r = 1. Cả V và T có tâm tại điểm (0, 0).

2. Sinh ra N điểm p có tọa độ (x, y), trong đó x, y là các số ngẫu nhiên và thuộc đoạn [-1, 1].
![](https://aivietnam.ai/wp-content/uploads/2019/07/pi_estimation.png)
3.  Đếm số điểm p thuộc T, gọi là NT
   
4. Cuối cùng, số PI được ước lượng như sau
> $$\pi \approx 4 \times  \frac{N_T}{N}$$

> Code:

```python
# Ước lượng số PI
import random
import math
N = 1000000

N_T = 0
for i in range(N):
    # Sinh ra tọa độ x,y thuộc đường tròn bán kính r=1
    x = 2*random.random()-1
    y = 2*random.random()-1
    if (math.sqrt(x**2+y**2<=1)):
        N_T +=1
print("Số Pi xấp xỉ:",4*N_T/N)
```
#### 2. Ước lượng số e

Số e được ước lượng dựa vào công thức sau:
> $$e = 1 + \frac{1}{1!}+\frac{1}{2!}+...+\frac{1}{n!}$$
> 
trong đó, n là số cho trước. n càng lớn thì độ chính xác càng cao.
### III. List trong python
Trong Python, list là một loại vùng chứa trong cấu trúc dữ liệu, được sử dụng để lưu trữ nhiều dữ liệu cùng một lúc. Danh sách trong Python được sắp xếp theo thứ tự và có số lượng xác định. Các phần tử trong danh sách được lập index theo một chuỗi xác định và việc lập index của danh sách được thực hiện với 0 là index đầu tiên.

Một danh sách có thể chứa các phần tử với kiểu dữ liệu như integer, float, string, boolean, cũng như Object. Danh sách cũng rất hữu ích để thực hiện cấu trúc dữ liệu Stack và Queue. Danh sách có thể thay đổi, chúng có thể được thay đổi ngay cả sau khi tạo.

Ví dụ: Danh sách tên của các học sinh trong lớp. Danh sách các mặt hàng trong cửa hàng, …..

**Cách tạo một danh sách.**
Trong lập trình Python, một danh sách được tạo bằng cách đặt tất cả các phần tử bên trong cặp dấu ngoặc vuông [ ], được phân tách bằng dấu phẩy. Nó có thể có bất kỳ số lượng các phần tử và các phần tử có thể có các kiểu dữ liệu khác nhau (số nguyên, float, chuỗi, v.v.). Cú pháp tạo một danh sách như sau
```python
<Tên_danh_sách> = [phần tử thứ 0, phần tử thứ 1, ... phần tử thứ n]
```

Ví dụ:
```python
# List cac so nguyen to nho hon 10
listPrimeNumber = [2,3,5,7]
# List cac trai cay
listFruit = [apple,mango,banana]
# List rong
listEmpty = []

```
**Cách truy cập danh sách.**

- Có nhiều cách khác nhau để ta có thể truy cập được các phần tử của danh sách. Gồm danh sách index xuôi và danh sách index ngược.

- Index xuôi: index được bắt đầu từ 0 gán vào phần tử đầu tiên của danh sách, phần tử tiếp theo được tăng lên 1 cho đến phần tử cuối cùng.

- Index ngược: index ngược giúp truy xuất dữ liệu từ phần từ cuối cùng ngược lại phần tử đầu tiên. Phần tử cuối cùng được đánh chỉ số -1, các phần tử tiếp theo trừ đi 1 cho đến phần tử đầu tiên của danh sách.

![](https://aivietnam.ai/wp-content/uploads/2019/07/lis_create1.png)
**List slicing**
Chúng ta có thể truy cập một loạt các phần tử trong danh sách bằng cách sử dụng kỹ thuật slicing (cắt) cho list.
![](https://aivietnam.ai/wp-content/uploads/2019/07/list_slicing.png)
**Thêm phần tử mới vào danh sách.**

Chúng ta có thể thêm một phần tử vào danh sách bằng phương thức `append()`.
![](https://aivietnam.ai/wp-content/uploads/2019/07/list_append.png)
Chúng ta cũng có thể sử dụng toán tử + để kết hợp (hay nối) hai danh sách.
![](https://aivietnam.ai/wp-content/uploads/2019/07/list_plus.png)
Toán tử * cho phép lặp lại một danh sách với số lần cho trước.
![](https://aivietnam.ai/wp-content/uploads/2019/07/list_mul.png)

Hơn nữa, chúng ta có thể chèn một phần tử tại một vị trí mong muốn bằng cách sử dụng phương thức insert() hoặc chèn nhiều mục bằng cách ép nó vào một lát trống của danh sách.

list.insert(index, element): index là vị trí mà một phần tử cần được chèn và element là phần tử được chèn vào danh sách.
![](https://aivietnam.ai/wp-content/uploads/2019/07/list_insert.png)
**Xóa phần từ khỏi danh sách.**

Chúng ta có thể xóa một hoặc nhiều mục khỏi danh sách bằng cách sử dụng từ khóa del. Nó thậm chí có thể xóa danh sách hoàn toàn.



Chúng ta có thể sử dụng phương thức remove() để xóa mục đã cho



hoặc phương thức pop() để xóa một mục tại chỉ mục đã cho



Chúng ta cũng có thể sử dụng phương thức clear () để làm trống danh sách
![](https://aivietnam.ai/wp-content/uploads/2019/07/list_clear.png)
Các hàm thông dụng thường khác
![](https://aivietnam.ai/wp-content/uploads/2019/07/list_index-768x305.png)
index() – Trả về vị trí đầu tiên

![](https://aivietnam.ai/wp-content/uploads/2019/07/list_index-768x305.png)

count() – Trả về số lần xuất hiện của một phần tử

![](https://aivietnam.ai/wp-content/uploads/2019/07/list_count.png)

sort() – Sắp xếp các phần tử



![](https://aivietnam.ai/wp-content/uploads/2019/07/list_sort.png)

reverse() – Đảo ngược vị trí các phần tử
![](https://aivietnam.ai/wp-content/uploads/2019/07/list_reverse.png)


copy() – copy một list

![](https://aivietnam.ai/wp-content/uploads/2019/07/list_copy.png)
### III. Xây dựng các hàm activation trong machine learning
Trong bài này, chúng ta sẽ tìm hiểu về các hàm activation phổ biến trong machine learning và cài đặt các hàm này với input là danh sách các giá trị số. Bảng sau thể hiện các công thức và đạo hàm của các hàm activation phổ biến.
![](https://aivietnam.ai/wp-content/uploads/2019/07/activation_table-768x397.png)
**1. Hàm sigmoid (logistic)**
Hàm sigmoid có hình dạng như sau:
![](https://aivietnam.ai/wp-content/uploads/2019/07/chap2_activation_sigmoid.png)
**Phân tích hàm sigmoid**

- Giá trị x∈R và y∈(0,1). Chúng ta có thể hình dùng hàm sigmoid giống như hàm ánh xạ từ (−∞,∞)↦(0,1).
- Hàm sigmoid là hàm không giảm (monotonic increasing), nghĩa là nếu x1≤x2 thì f(x1)≤f(x2). Chúng ta thường dùng tính chất này khi chúng ta quan tâm đến thứ tự lớn hơn, nhỏ hơn, hơn là giá trị độ lớn của chúng.
- Hàm sigmoid có độ dốc (tương đương với đạo hàm) lớn xung quanh giá trị x=0 và độ dốc rất nhỏ ở 2 đầu. Điều này gây ra vấn đề khi tính toán dựa vào giá trị đạo hàm. Vì giá trị đạo hàm quả nhỏ nên hầu như nó không có hữu ích gì.

Ví dụ về tính sigmoid cho một danh sách các số.
