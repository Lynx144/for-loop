# x = int(input('Nhập số:'))
# for a in range (0,x):
#     for b in range (1,x+1):
#         print(a*x+b,sep=' ',end=' ')
#     print()
#O(n)=X^2
#C2
n = int(input('Nhập số:'))
b= 0

for a in range(1,n*n+1):
    if b < n:
        print(a,end=' ')
        b +=1
        if b == n:
            b = 0
            print()