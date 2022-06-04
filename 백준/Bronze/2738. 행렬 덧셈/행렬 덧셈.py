sero, garo = map(int, input().split())
tmp = []


ary1 = []
for i in range(sero):
    for k in map(int, input().split()):
        tmp.append(k)
    ary1.append(tmp)
    tmp = []


ary2 = []
for i in range(sero):
    for k in map(int, input().split()):
        tmp.append(k)
    ary2.append(tmp)
    tmp = []


for i in range(sero):
    ans = []
    for j in range(garo):
        ans.append(ary1[i][j]+ary2[i][j])
    print(" ".join(map(str, ans)))
