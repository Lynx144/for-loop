#C1
# x = (input("nhập chữ :"))
# a =0
# for y in x.lower():
#     if y in {'a', 'e', 'i', 'o', 'u'}:
#         a += 1
# print(a)
#C2
str = input('Nhập chữ: ')
x = 0
for y in str.lower():
    if y == "a" or y == "e" or y == "i" or y == "o" or y == "u":
        x +=1
print(x)