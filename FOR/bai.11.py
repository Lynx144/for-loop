x = int(input('Nhập số nguyên dương:'))
for y in range(2,x+1):
    if y % 2 != 0 and y % 3 != 0 and y % 5 !=0 and y % 10 != 1 :
        print(y)
    elif y == 3 or y == 5:
        print(y)