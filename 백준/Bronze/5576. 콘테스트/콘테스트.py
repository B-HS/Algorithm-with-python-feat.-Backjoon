for i in range(2):
    ary = []
    for p in range(10):
        ary.append(int(input()))
    print(sum(sorted(ary)[-3:]), end=" ")

