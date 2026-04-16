#Định nghĩa hàm kiểm tra số nguyên tố is_prime(n)
def is_prime(n):
    # Quy ước cơ bản: Số nguyên tố phải là số nguyên lớn hơn 1
    # Nếu n nhỏ hơn hoặc bằng 1 (như 0, 1, -5...), chắc chắn không phải số nguyên tố
    if n <= 1:
        return False
    
    # Dùng vòng lặp kiểm tra các số từ 2 đến n-1 theo đúng gợi ý
    # Lệnh range(2, n) sẽ tự động dừng lại ở n-1
    for i in range(2, n):
        # Nếu n chia hết cho i (phần dư bằng 0)
        if n % i == 0:
            # Phát hiện có ước số khác 1 và chính nó!
            # Lập tức trả về False và THOÁT KHỎI HÀM ngay lập tức.
            return False
            
 # Nếu vòng lặp chạy xong hết (từ 2 đến n-1) mà không bị thoát giữa chừng
# Nghĩa là n không chia hết cho bất kỳ số nào cả -> Nó là số nguyên tố
    return True

#code bên ngoài gọi hàm để in các số nguyên tố từ 1 đến 100
print("Các số nguyên tố từ 1 đến 100 là:")

# Vòng lặp duyệt các số từ 1 đến 100 (range kết thúc ở 101)
for so in range(1, 101):
# Đem từng 'so' bỏ vào "cỗ máy" is_prime để kiểm tra
    if is_prime(so) == True:
# Nếu máy trả về True, in số đó ra
# end=" " giúp in các số cách nhau bởi khoảng trắng trên cùng 1 dòng
        print(so, end=" ")