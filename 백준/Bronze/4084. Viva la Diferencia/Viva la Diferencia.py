while 1:
    a, b, c, d = map(int, input().split())
    if a == b == c == d == 0:
        break
    ans=0
    while not (a == b == c == d):
        a, b, c, d = abs(a-b), abs(b-c), abs(c-d), abs(d-a)
        ans += 1
    print(ans)
        