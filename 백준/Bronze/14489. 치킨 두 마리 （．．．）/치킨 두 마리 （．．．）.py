a, b = map(int, input().split())
c = int(input())
print(a+b if (a+b)-(2*c) < 0 else (a+b)-(2*c))