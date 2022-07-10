ary = [100, 100, 200, 200, 300, 300, 400, 400, 500]
ans = list(map(int, input().split()))
sm = 0
for i in range(9):
    if ary[i] < ans[i]:
        print("hacker")
        exit(0)
    sm += ans[i]
if sm >= 100:
    print("draw")
else:
    print("none")