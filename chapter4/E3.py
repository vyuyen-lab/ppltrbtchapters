class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    def calculate_salary(self):
        return "Undefined"

class FullTimeEmployee(Employee):
    def __init__(self, emp_id, name, base_salary):
        super().__init__(emp_id, name) 
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary

class PartTimeEmployee(Employee):
    def __init__(self, emp_id, name, work_hours, hourly_rate):
        super().__init__(emp_id, name)
        self.work_hours = work_hours
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.work_hours * self.hourly_rate


class EmployeeManager:
    def __init__(self):
        self.employee_list = []

    def add_employee(self, employee):
        self.employee_list.append(employee)
        print(f"[*] Đã thêm nhân viên: {employee.name}")

    def display_salaries(self):
        if not self.employee_list:
            print("Danh sách hiện đang trống!")
            return
            
        print(" BẢNG LƯƠNG NHÂN VIÊN ")
        for emp in self.employee_list:
            print(f"Tên: {emp.name} | Lương: ${emp.calculate_salary()}")
        print("----------------------------")

    def start_menu(self):
        while True:
            print(" QUẢN LÝ NHÂN VIÊN ")
            print("1. Thêm nhân viên Full-Time")
            print("2. Thêm nhân viên Part-Time")
            print("3. In bảng lương tất cả nhân viên")
            print("4. Thoát chương trình")
            
            choice = input("Nhập lựa chọn của bạn (1-4): ")

            if choice == '1':
                emp_id = input("Nhập ID: ")
                name = input("Nhập tên: ")
                base_salary = float(input("Nhập lương cơ bản: "))
                new_emp = FullTimeEmployee(emp_id, name, base_salary)
                self.add_employee(new_emp)
                
            elif choice == '2':
                emp_id = input("Nhập ID: ")
                name = input("Nhập tên: ")
                work_hours = float(input("Nhập số giờ làm: "))
                hourly_rate = float(input("Nhập mức lương/giờ: "))
                new_emp = PartTimeEmployee(emp_id, name, work_hours, hourly_rate)
                self.add_employee(new_emp)
                
            elif choice == '3':
                self.display_salaries()
                
            elif choice == '4':
                print("Đang thoát chương trình. Tạm biệt")
                break
            else:
                print("Lựa chọn không hợp lệ, vui lòng nhập lại")

if __name__ == "__main__":
    system = EmployeeManager()
    system.start_menu()
