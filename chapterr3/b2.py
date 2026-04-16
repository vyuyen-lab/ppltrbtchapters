n = int(input("Nhập số nguyên dương n: "))
tong_le = 0
tong_chan = 0
for i in range(1, n + 1):

    if i % 2 == 0:
    
        tong_chan = tong_chan + i
    else:
        tong_le = tong_le + i
print("Tổng các số lẻ từ 1 đến", n, "là:", tong_le)
print("Tổng các số chẵn từ 1 đến", n, "là:", tong_chan)