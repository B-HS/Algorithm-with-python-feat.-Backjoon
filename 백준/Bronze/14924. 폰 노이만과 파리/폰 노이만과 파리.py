a, b, c = map(int, input().split())
ans = c//(a*2) * b
#풀기 전 구하려는 시간은 = c/(2*a)이다,  시간에 속도를 곱하면 거리가됨므로 c/(2*a)*b = 파리의 이동거리가 된다
print(ans)