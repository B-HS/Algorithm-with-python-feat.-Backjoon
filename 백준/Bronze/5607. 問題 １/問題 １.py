ans1, ans2 = 0, 0
for i in range(int(input())):
    a, b = map(int,input().split())
    if a > b:
        ans1 += a+b
    elif a<b:
        ans2 += a+b
    else:
        ans1 +=a
        ans2 +=b
print(ans1, ans2)