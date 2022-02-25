for i in range(int(input())):
    s,e = map(int,input().split())
    geori = e-s #거리
    a = 0 #제곱비교수

    while(1):
        if geori <= a*(a+1): # 경계선이되는 제곱a를 구함
            break
        a+=1
    if geori <= a**2:# 거리가 a제곱근보다 작으면
        print(a*2-1) # a제곱의 -1, 위에서부터 아래로 정렬시 a값제곱의 위에있으므로 -1을 출력
    else: # 크면
        print(a*2) # 아래에 열거될 리스트에 있으므로 그냥 출력


