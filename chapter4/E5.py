class Pet:
    def __init__(self, pet_id, name, species, price):
        self.__pet_id = pet_id
        self.__name = name
        self.__species = species
        self.__price = price

    def get_pet_id(self):
        return self.__pet_id

    def get_price(self):
        return self.__price

    def display_info(self):
        print(f"ID: {self.__pet_id} | Tên: {self.__name} | Giống: {self.__species} | Giá: ${self.__price}")

class StoreService:
    def __init__(self):
        self.inventory = []  
        self.revenue = 0.0   

    def add_pet(self, pet):
        self.inventory.append(pet)
        print("[+] Đã thêm thú cưng vào cửa hàng thành công!")

    def view_inventory(self):
        if not self.inventory:
            print("Cửa hàng hiện tại chưa có thú cưng nào.")
            return
            
        print(" DANH SÁCH THÚ CƯNG TRONG KHO ")
        for pet in self.inventory:
            pet.display_info()
        print("------------------------------------")

    def sell_pet(self, pet_id):
        for pet in self.inventory:
            if pet.get_pet_id() == pet_id: 
                self.revenue += pet.get_price()
                self.inventory.remove(pet)
                print(f"[!] Bán thành công! Đã thu về ${pet.get_price()}")
                return 
            
        print(f"[-] Không tìm thấy thú cưng nào có ID: {pet_id}")


class ConsoleView:
    def __init__(self):
        self.service = StoreService()

    def start(self):
        while True:
            print(" QUẢN LÝ CỬA HÀNG THÚ CƯNG ")
            print("1. Thêm thú cưng mới")
            print("2. Xem kho hàng")
            print("3. Bán thú cưng")
            print("4. Xem tổng doanh thu")
            print("5. Thoát")
            
            choice = input("Nhập lựa chọn (1-5): ")
            
            if choice == '1':
                p_id = input("Nhập ID: ")
                name = input("Nhập tên: ")
                species = input("Nhập giống loài (Chó/Mèo/Chim...): ")
                price = float(input("Nhập giá tiền: "))
                
                new_pet = Pet(p_id, name, species, price)
                self.service.add_pet(new_pet)
                
            elif choice == '2':
                self.service.view_inventory()
                
            elif choice == '3':
                p_id = input("Nhập ID thú cưng muốn bán: ")
                self.service.sell_pet(p_id)
                
            elif choice == '4':
                print(f"\n[$$$] Tổng doanh thu hiện tại: ${self.service.revenue}")
                
            elif choice == '5':
                print("Đóng cửa hàng. Tạm biệt!")
                break
            else:
                print("Lựa chọn không hợp lệ!")


if __name__ == "__main__":
    app = ConsoleView()
    app.start()