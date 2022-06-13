a, b = map(int, input().split())
b = float("0."+str(b))
print(0 if a-(a*b) >= 100 else 1)