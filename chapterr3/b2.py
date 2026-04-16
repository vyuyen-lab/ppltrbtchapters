# 1. Nhập vào một số nguyên dương n
n = int(input("Nhập số nguyên dương n: "))

# 2. Khởi tạo trạng thái ban đầu
# Ban đầu chưa đếm gì cả nên tổng chẵn và tổng lẻ đều bằng 0
tong_le = 0
tong_chan = 0

# 3. Vòng lặp For chạy từ 1 đến n
# Lưu ý: range(1, n + 1) sẽ chạy từ 1 và dừng lại ở n
for i in range(1, n + 1):
    
    # Kiểm tra xem i chia lấy dư cho 2 có bằng 0 không (tức là số chẵn)
    if i % 2 == 0:
        # Nếu là số chẵn, lấy tổng chẵn cũ cộng thêm i để ra tổng chẵn mới
        tong_chan = tong_chan + i
    else:
        # Ngược lại (là số lẻ), cộng i vào tổng lẻ
        tong_le = tong_le + i

# 4. In kết quả ra màn hình bằng cú pháp đơn giản nhất
print("Tổng các số lẻ từ 1 đến", n, "là:", tong_le)
print("Tổng các số chẵn từ 1 đến", n, "là:", tong_chan)