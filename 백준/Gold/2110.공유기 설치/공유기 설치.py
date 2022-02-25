#거리를 mid값으로 찾는 문제
import sys
input=sys.stdin.readline
n, c = map(int,input().split())
ary=sorted([int(input()) for i in range(n)])
ans = []
start = 1 #최소값 1 
end = ary[-1]-ary[0] # 중간값을 위한 max값
while start <= end: #이분시작
    mid=(start+end)//2 #mid값
    tmp = ary[0] # 첫값은 0값
    cnt = 1 #0값넣었으니 cnt = 1

    for i in range(n): # 거리값으로 공유기 찾기 시작
        if ary[i] >= tmp + mid: # 직전값과 mid값을 더한게 ary[i]보다 크면(거리에 공유기들어간값)
            cnt +=1 # ㅇㅋ 크네 들어갈수있다 cnt +1해주고
            tmp = ary[i]   # tmp의 직전값은 다시 들어간값으로 , 그리고 for문 반복
              
    if cnt >=c : #설치한게 제시된 공유기 개수값보다 많으니
        ans.append(mid) #ㅇㅋ 넌 일단 후보 그러니 일단 넣어
        start = mid+1 #오 되네 일단 안끝났으니 mid+1로 해서start 다시돌려
    else: # 어? 할당량없네 ??
        end = mid-1 # ㅇㅋ 우측에는 찾는 값 없다 범위줄여


print(max(ans)) #ans에서 두 공유기 사이의 최대 거리뽑아와서 출력