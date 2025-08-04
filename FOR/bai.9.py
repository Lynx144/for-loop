x = int(input("Nhập số nguyên dương:"))
y = 0
a = 1
b = 0
for z in range(1,x) :
    b = y + a
    a = y
    y = b
print(b)