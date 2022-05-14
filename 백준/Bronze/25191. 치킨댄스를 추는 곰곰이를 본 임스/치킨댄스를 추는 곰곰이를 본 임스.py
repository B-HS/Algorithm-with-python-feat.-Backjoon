a = int(input())
b, c = map(int, input().split())


total = (b//2)+c
print(total if  total<= a else a)