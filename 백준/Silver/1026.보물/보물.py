num = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
ans = 0
for i in range (num):
    ans += a.pop(a.index(min(a)))*b.pop(b.index(max(b))) # a최소, b최대 빼서 곱해서 넣은 뒤 ans+=
print(ans)
