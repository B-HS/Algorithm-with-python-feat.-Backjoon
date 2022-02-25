import sys
su = int(sys.stdin.readline())
ary= list(map(int, sys.stdin.readline().split()))
tary = sorted(list(set(ary))) # 1000 999, 2 4 -10 - 9
dic = {tary[i]:i for i in range(len(tary))}
for i in ary:
    print(dic[i], end=" ")