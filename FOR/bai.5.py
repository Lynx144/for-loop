x = int(input("nhập số nguyên dương:"))
y = 0
for z in range(1,x+1):
    for a in range(1,11):
        y = z*a
        print(f"{z}*{a}={y}")