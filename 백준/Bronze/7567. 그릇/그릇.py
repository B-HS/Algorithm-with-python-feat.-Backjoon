tmp = ""
ans = 0
for i in input():
    if tmp == i:
        ans += 5
        tmp = i
    else:
        ans += 10
        tmp = i
print(ans)
