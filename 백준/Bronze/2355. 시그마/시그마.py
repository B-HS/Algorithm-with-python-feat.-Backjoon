ary = sorted(list(map(int,input().split()))) # 숫자 받아와서 순서대로 넣기
print(int(sum(ary)*((ary[1]-ary[0]+1)/2))) # 시그마식 (a+b) * (a-b+1)/2 출력