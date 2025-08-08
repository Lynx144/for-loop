a = int(input('Nhập số nguyên dương:'))
b = int(input('Nhập số nguyên dương:'))
while b != 0:
    a, b = b, a % b

print(a)