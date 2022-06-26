a, b, c, d = map(int, input().split())
e = a/b*c/d
print(1 if (e/2 == e//2) else 0)