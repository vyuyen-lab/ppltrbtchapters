class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder  
        self.__balance = balance              
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"[+] Đã nạp thành công ${amount}. Số dư mới: ${self.__balance}")
        else:
            print("[!] Lỗi: Số tiền nạp phải lớn hơn 0.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"[-] Đã rút thành công ${amount}. Số dư còn lại: ${self.__balance}")
        elif amount > self.__balance:
            print("[!] Lỗi: Rút tiền thất bại. Số dư trong tài khoản không đủ")
        else:
            print("[!] Lỗi: Số tiền rút phải lớn hơn 0.")

    def get_balance(self):
        return self.__balance


print(" TẠO TÀI KHOẢN ")
my_account = BankAccount("Vy Uyên") 
print(f"Chủ tài khoản: {my_account.account_holder}")
print(f"Số dư ban đầu: ${my_account.get_balance()}")

print(" GIAO DỊCH NẠP TIỀN ")
my_account.deposit(500)   
my_account.deposit(-50)   

print(" GIAO DỊCH RÚT TIỀN ")
my_account.withdraw(200)  
my_account.withdraw(1000) 

print(" KIỂM TRA TÍNH ĐÓNG GÓI ")
print(f"Tên chủ thẻ (Public): {my_account.account_holder}")
print("Không thể truy cập trực tiếp my_account.__balance từ bên ngoài!")