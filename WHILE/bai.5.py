n = int(input("Nhập một số: "))
kq =0
while n != 0:
    t = n % 10
    kq = kq * 10 + t
    n //= 10
print(kq)