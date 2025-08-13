n = int(input("Nhập một số: "))
i = 0
while n != 0:
    i += n%10
    n = n//10
print(i)