_ = input()
ary = list(map(int, input().split()))

num = 0
ans = 0
if ary[0] == 1:
    num = 1
    ans += 1
for i in range(1, len(ary)):
    if ary[i] == 1 and ary[i-1] == 1:
        num += 1
    elif ary[i] == 1:
        num = 1
    else:
        num = 0
    ans += num

print(ans)
