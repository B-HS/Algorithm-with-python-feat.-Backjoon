n, k = map(int,input().split())
ary = [int(input()) for _ in range(n)]
dp = [0]*(k+1)
dp[0] = 1
for i in ary:
    for p in range(1, k+1):
        if p-i>=0:
            dp[p]+=dp[p-i]

print(dp[-1])