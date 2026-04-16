def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            
            return False
            
    return True

print("Các số nguyên tố từ 1 đến 100 là:")

for number in range(1, 101):
    if is_prime(number):
        print(number, end=" ") 