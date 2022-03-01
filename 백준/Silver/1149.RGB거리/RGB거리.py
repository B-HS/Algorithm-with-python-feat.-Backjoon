ary=[]
for i in range(int(input())):
    ary.append(list(map(int,input().split())))
for i in range(1, len(ary)):
    ary[i][0] = ary[i][0]+ min(ary[i-1][1], ary[i-1][2])
    ary[i][1] = ary[i][1]+ min(ary[i-1][0], ary[i-1][2])
    ary[i][2] = ary[i][2]+ min(ary[i-1][0], ary[i-1][1])

print(min(ary[len(ary)-1][0], ary[len(ary)-1][1], ary[len(ary)-1][2]))