import sys
input=sys.stdin.readline
answer=0
for i in range(int(input())-1):
    answer+=int(input())-1
print(answer+int(input()))