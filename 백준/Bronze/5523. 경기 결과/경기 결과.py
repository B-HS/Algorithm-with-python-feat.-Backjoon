import sys
input = sys.stdin.readline
left, right = 0, 0
for i in range(int(input())):
    a, b = map(int,input().split())
    if a> b:
        left+=1
    elif a<b:
        right+=1

print(left, right)