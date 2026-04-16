def cong(a, b):
    return a + b

def tru(a, b):
    return a - b

def nhan(a, b):
    return a * b

def chia(a, b):
    if b == 0:
        return "Lỗi chia cho 0"
    else:
        return a / b

def hien_thi_menu():
    print("\n--- MÁY TÍNH BỎ TÚI ---")
    print("1. Cộng")
    print("2. Trừ")
    print("3. Nhân")
    print("4. Chia")
    print("5. Thoát")

while True:
    hien_thi_menu()
    
    lua_chon = input("Mời bạn chọn (1-5): ")

    if lua_chon == '5':
        print("Đang thoát chương trình... Tạm biệt!")
        break  # Kết thúc vòng lặp
    
    if lua_chon in ['1', '2', '3', '4']:
        a = float(input("Nhập số thứ nhất (a): "))
        b = float(input("Nhập số thứ hai (b): "))

        if lua_chon == '1':
            print("Kết quả:", cong(a, b))
        elif lua_chon == '2':
            print("Kết quả:", tru(a, b))
        elif lua_chon == '3':
            print("Kết quả:", nhan(a, b))
        elif lua_chon == '4':
            print("Kết quả:", chia(a, b))
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")