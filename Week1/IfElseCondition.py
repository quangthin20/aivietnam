# @author: Quang Thin - AI Vietnam


'''
Đề bài: viết hàm tong nhằm tính giá tiền được giảm cho khách mua hàng.
Khi tổng số tiền mua hàng lớn hơn hoặc bằng 2000 thì khách hàng sẽ được giảm 20%. 
Khi tổng số tiền mua hàng nằm trong khoảng [1000, 2000) thì khách hàng sẽ được giảm 10%,
và dưới 1000 sẽ giảm 5%.
'''

def discount(total_cost):
    # Trên 2000, giảm 20 phần trăm
    if total_cost>=2000:
        discount = total_cost*0.2
    # Trên 1000, giảm 10%
    elif total_cost>=1000:
        discount = total_cost*0.1
    # Dưới 1000 giảm 5%
    else:
        discount = total_cost*0.05
    return discount

total_cost = int(input("Nhập số tiền bạn đã mua:"))

print("Bạn được giảm {}".format(discount(total_cost)))
