#https://namu.wiki/w/%EC%B5%9C%EC%9E%A5%20%EC%A6%9D%EA%B0%80%20%EB%B6%80%EB%B6%84%20%EC%88%98%EC%97%B4#s-3.2
#이진탐색을 활용을 해서 정확한 배열을 찾을 필요 없이 그냥 냅다 작은 수부터 때려넣기 
import sys
input=sys.stdin.readline
n=int(input())
ary=list(map(int, input().split()))
dp=[0]
for i in range(n): 
    start = 0
    end = len(dp)-1
    while start <=end:
        mid = (start+end)//2
        if dp[mid]<ary[i]:
            start = mid +1
        else:
            end = mid-1
    if len(dp)<=start:
        dp.append(ary[i])
    else:
        dp[start]= ary[i]


print(len(dp)-1)