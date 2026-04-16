
ds_so = [1, 2, 5, 6, 8, 12, 13, 14, 15, 20]
print("Danh sách ban đầu là:", ds_so)

ds_so.append(25)
print("Danh sách sau khi thêm số 25 là:", ds_so)

ds_so[2] = 10 
print("Danh sách sau khi sửa phần tử thứ 3 thành 10 là:", ds_so)

del ds_so[-1]
print("Danh sách sau khi xoá phần tử cuối cùng là:", ds_so)

tong = sum(ds_so)
print("Tổng các phần tử trong danh sách là:", tong)