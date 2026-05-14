class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.status = "Available" 

    def display_info(self):
        print(f"ID: {self.book_id} | Tên sách: {self.title} | Tác giả: {self.author} | Trạng thái: {self.status}")

class LibraryManager:
    def __init__(self):
        self.book_list = []

    def add_book(self, new_book):
        self.book_list.append(new_book)
        print(f"[*] Đã thêm sách '{new_book.title}' thành công!")

    def display_all(self):
        if not self.book_list:
            print("Thư viện hiện đang trống.")
            return
            
        print(" DANH SÁCH THƯ VIỆN ")
        for book in self.book_list:
            book.display_info()
        print("--------------------------")

    def borrow_book(self, book_id):
        for book in self.book_list:
            if book.book_id == book_id:
                if book.status == "Available":
                    book.status = "Borrowed"  
                    print(f"[+] Mượn sách '{book.title}' thành công!")
                else:
                    print(f"[-] Rất tiếc, sách '{book.title}' đã có người mượn.")
                return 
        print(f"[!] Lỗi: Không tìm thấy sách với ID '{book_id}'.")

def main():
    manager = LibraryManager()
    
    while True:
        print("\n=== QUẢN LÝ THƯ VIỆN ===")
        print("1. Thêm sách mới")
        print("2. Hiển thị tất cả sách")
        print("3. Mượn sách")
        print("4. Thoát chương trình")
        
        choice = input("Nhập lựa chọn của bạn (1-4): ")
        
        if choice == '1':
            b_id = input("Nhập ID sách: ")
            title = input("Nhập tên sách: ")
            author = input("Nhập tác giả: ")

            new_book = Book(b_id, title, author)
            manager.add_book(new_book)
            
        elif choice == '2':
            manager.display_all()    
        elif choice == '3':
            b_id = input("Nhập ID sách muốn mượn: ")
            manager.borrow_book(b_id)
        elif choice == '4':
            print("Đang thoát chương trình. Tạm biệt!")
            break   
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại!")

if __name__ == "__main__":
    main()