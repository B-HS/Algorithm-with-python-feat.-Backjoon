arysize=int(input())
mx = int(input())
start, end = 1, mx
while start <= end:
    mid = (start+end)//2
    tmp = 0
    for i in range(1, arysize+1):
        tmp += min(mid//i, arysize)
    
    if tmp >=mx:
        ans = mid
        end = mid-1
    else:
        start = mid +1

print(ans)