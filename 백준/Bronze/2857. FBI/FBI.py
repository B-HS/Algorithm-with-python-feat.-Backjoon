li = [] 
#범위는 정해져있고
for i in range(1, 6): 
    w = input() 
    #따로비교보단 그냥 문자열을 줘서 비교
    if "FBI" in w: 
        li.append(i) 
        #있으면 풀어쓰고
if li: 
    print(*li) 
    # 리스트없으면 없다출력
else: 
    print("HE GOT AWAY!")