def add_contact(danh_ba):
    ten = input("Nhập tên: ")
    sdt = input("Nhập số điện thoại: ")
    lien_he = ten + " - " + sdt
    danh_ba.append(lien_he)
    print("Thêm thông báo thành công!")

def show_contacts(danh_ba):
    if len(danh_ba) == 0:
        print("Chưa có liên hệ nào.")
    else:
        print("\n--- DANH SÁCH LIÊN HỆ ---")
        for i, lien_he in enumerate(danh_ba, start=1):
            print(str(i) + ". " + lien_he)

def find_contact(danh_ba): 
    
    for lien_he in danh_ba:
        if ten_can_tim.lower() in lien_he.lower():
            print("Thông tin tìm thấy:", lien_he)
            tim_thay = True
    
    if not tim_thay:
        print("Không tìm thấy.")
def main():
    my_contacts = [] 
    
    while True:
        print("\n=== HỆ THỐNG QUẢN LÝ DANH BẠ ===")
        print("1. Thêm liên hệ mới")
        print("2. Hiển thị tất cả danh bạ")
        print("3. Tìm kiếm liên hệ")
        print("4. Thoát chương trình")
        
        lua_chon = input("Mời chọn chức năng (1-4): ")
        
        if lua_chon == "1":
            add_contact(my_contacts)
        elif lua_chon == "2":
            show_contacts(my_contacts)
        elif lua_chon == "3":
            find_contact(my_contacts)
        elif lua_chon == "4":
            print("Đang thoát... Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ!")

main()