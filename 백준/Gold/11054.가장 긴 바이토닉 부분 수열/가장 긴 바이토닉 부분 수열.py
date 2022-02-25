n=int(input())
ary=list(map(int, input().split())) # 1 5 2 1 4 3 4 5 2 1
dp=[1]*n
r_dp=[1]*n
ans = [0]*n
for i in range(n): #증가하는 수열 찾아서 dp에 넣기 # 1 2 3 4 5
  for p in range(i):
    if ary[p]<ary[i]:  
        dp[i]=max(dp[i],dp[p]+1) 

for i in range(n, -1, -1): #역순으로 돌려서감소하는 수열 찾아서 dp에 넣기
    for p in range(n-1, i, -1):
        if ary[p]<ary[i]:  
            r_dp[i]=max(r_dp[i],r_dp[p]+1) 

for i in range(n): #각 수열을 더한값을 ans 에 넣기
    ans[i] = dp[i] + r_dp[i] -1

print(max(ans))