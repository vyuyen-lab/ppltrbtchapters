
ds_so = [1, 2, 5, 6, 8, 12, 13, 14, 15, 20]
print("Danh sách ban đầu là:", ds_so)

# Sử dụng hàm .append() để "đính" thêm phần tử vào cuối
ds_so.append(25)
print("Danh sách sau khi thêm số 25 là:", ds_so)

# Sửa giá trị của phần tử thứ 3 (chỉ số index là 2)
ds_so[2] = 10 
print("Danh sách sau khi sửa phần tử thứ 3 thành 10 là:", ds_so)

#Xoá phần tử cuối cùng của danh sách
# Sử dụng lệnh del kết hợp với chỉ số -1 (chỉ số -1 luôn là phần tử cuối cùng)
del ds_so[-1]
print("Danh sách sau khi xoá phần tử cuối cùng là:", ds_so)

# Python có sẵn hàm sum() rất tiện lợi để cộng tất cả các số trong list
tong = sum(ds_so)
print("Tổng các phần tử trong danh sách là:", tong)