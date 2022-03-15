answer = []
for i in range(int(input())):
    ary = list(map(int, input().split()))
    for p in ary:
        if p % 2 == 0:
            answer.append(p)
    print(sum(answer), min(answer))
    answer = []
