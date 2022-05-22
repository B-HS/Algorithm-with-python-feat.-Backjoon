import sys
input = sys.stdin.readline
sosu = 1
fo = int(input())
ary = set(map(int, input().split()))
# for i in range(fo):
#     num = ary[i]


def sosuni(num):
    if num in [2, 3, 5, 7]:
        return True
    for i in range(2, int(k**0.5)+1):

        if num % i == 0:
            return False
    return True


for k in ary:
    if sosuni(k) == True:
        # for j in range(1, int(k**0.5)):
        #     if k in [2, 3, 5, 7]:
        #         # sosu.add(str(2))
        #         sosu *= k
        #         break
        #     if k % j == 0:
        #         break
        #     # sosu.add(str(k))

        sosu *= k


print(sosu if sosu != 1 else -1)
# print(eval("*".join(sosu)) if len(sosu) > 0 else -1)
