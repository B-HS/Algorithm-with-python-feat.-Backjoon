import sys

num = int(sys.stdin.readline())
ary = []

for i in range(num):
    temp = sys.stdin.readline().strip()
    ary.append((temp, len(temp)))
ary = list(set(ary))
ary.sort(key=lambda x:(x[1], x[0]))


for i in ary:
    print (i[0])