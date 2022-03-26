n=int(input())
ary = sorted([list(map(int,input().split())) for _ in range(n)])
dp = [1]*n
for i in range(n):
    for p in range(i):
        if ary[i][1] > ary[p][1]:
            dp[i] = max(dp[i], dp[p]+1)
print (n-max(dp))
