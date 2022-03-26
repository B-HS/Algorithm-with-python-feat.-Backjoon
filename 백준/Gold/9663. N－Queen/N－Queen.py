def check(tmp): #윗라인 체크
    for p in range(tmp):
        if ary[tmp] == ary[p] or abs(ary[tmp] - ary[p]) == abs(tmp-p):#생성된 윗라인에 있으면 
            return False#false
    return True#아님 true
    
def back(tmp):
    global ans
    if tmp == nq:#tmp가 거르고 걸러 결국 nq값까지왔다면
        ans +=1 #ans에 +=1
    else:
        for i in range(nq): # 빽뜨뤠킹 0~3
            ary[tmp] = i # 첫줄에 몇번째 칸에 들어갈 것인가 
            if check(tmp): # 들어간거 윗라인체크해서
                back(tmp+1) # True면 tmp+1해서 다음줄로

nq = int(input())
ary = [0]*nq
ans = 0
back(0)
print(ans)