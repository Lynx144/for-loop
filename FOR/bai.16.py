x = 0
while True:
    a = int(input('nhập một số (bấm số 1 để ngừng):'))
    if a <= 1 :
        break
    x +=a
print(f'Tổng các số bạn nhập là:{x}')
