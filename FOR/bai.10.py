x = int(input("Nhập số nguyên dương:"))
y=0
for z in range(1,x):
    if x % z == 0 :
        y = z + y
        if y == x :
            print("YES")
if y != x:
    print("NO")