hap = 0
ary = list(map(int,input().split()))
for i in range(len(ary)):
    hap += ary[i]*5
print(hap)