x = int(input("Nhập một số nguyên dương:"))
so_chan = 0
so_le = 0
for a in range(1,x+1):
    if a % 2 == 0:
        so_chan = so_chan + 1
    else:
        so_le = so_le + 1
print(f"số lượng số lẻ là:{so_le}")
print(f"số lượng số chẵn là:{so_chan}")
