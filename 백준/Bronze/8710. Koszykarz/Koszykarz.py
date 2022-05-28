a, b, c = map(int, input().split())
tar = b-a
print(tar//c if tar % c == 0 else tar//c+1)