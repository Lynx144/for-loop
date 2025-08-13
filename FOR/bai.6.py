S = input("hãy nhập một chữ tiếng anh:")
t = ""
# C1
# if S[::-1] == S :
#     print("YES")
# else:
#     print("NO")
for i in range(len(S)-1,-1,-1):
    t += S[i]
if t == S:
    print("YES")
else:
    print("NO")
