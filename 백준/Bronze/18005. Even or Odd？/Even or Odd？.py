n = int(input())
if n % 2 == 1:
    print(0)
else:
    print(2 if (n//2) % 2 == 0 else 1)