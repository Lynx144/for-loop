x = int(input("Nhập số nguyên dương:"))
y = 0
for z in range(1,x+1):
    if z % 2 == 0:
        y = y + z
print(f"Tổng các số chẵn là:{y}")
