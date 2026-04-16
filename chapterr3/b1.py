#Viết chương trình tính cước taxi dựa trên số ki-lô-mét ( ) nhập từ bàn phím. Biết quy tắc
#tính giá như sau:
# ● 1 km đầu tiên: 15.000 VNĐ.
# ● Từ km thứ 2 đến km thứ 20: 12.000 VNĐ / km.
# ● Từ km thứ 21 trở đi: 10.000 VNĐ / km.
# Yêu cầu: In ra số tiền khách phải trả (có sử dụng rẽ nhánh if-elif-else).

km = float(input("Nhập số km: "))
if km <= 1:
    tien = 15000
elif km <= 20:
    tien = 15000 + (km - 1) * 12000
else:
# 243.000 là tổng tiền cố định của 20km đầu (15.000 + 19 * 12.000)
    tien = 243000 + (km - 20) * 10000
# In ra kết quả một cách đơn giản nhất, không dùng các cú pháp format phức tạp
print("Số tiền phải trả là:", tien, "VNĐ")