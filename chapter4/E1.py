class Rectangle:
    
    def __init__(self, length, width):
        self.length = length  
        self.width = width   

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

    def calculate_area(self):
        return self.length * self.width

rect1 = Rectangle(15, 5)   
rect2 = Rectangle(25, 2)  

print(" Hình chữ nhật I ")
print(f"Chu vi: {rect1.calculate_perimeter()}")
print(f"Diện tích: {rect1.calculate_area()}")

print(" Hình chữ nhật II ")
print(f"Chu vi: {rect2.calculate_perimeter()}")
print(f"Diện tích: {rect2.calculate_area()}")