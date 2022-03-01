count = 0
ans = 0
for i in range (int(input())):
    ary = list(input())
    for z1 in range(len(ary)-1):    
        if ary[z1] != ary[z1+1]:
            if ary[z1] in ary[z1+1:]:
                count +=1
            
    if count == 0:
        ans += 1
    else:
        count = 0
print(ans)
