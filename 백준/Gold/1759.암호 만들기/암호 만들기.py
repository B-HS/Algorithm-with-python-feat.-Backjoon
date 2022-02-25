def back(tmp):
    if len(ans)==n:
        mo = 0
        za = 0
        for i in range(n):
            if ans[i] in 'aeiou':
                mo+=1
            else:
                za+=1
        if mo>=1 and za>=2:
            print (''.join(ans))
        return

    for i in range(tmp, k):
        if ary[i] not in ans:
            ans.append(ary[i])
        back(i+1)
        ans.pop()


n,k = map(int,input().split())
ary = sorted(list(map(str,input().split())))
ans = []
back(0)