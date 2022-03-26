from collections import deque
import sys

revcnt = False
for i in range(int(input())):
    cnt = 0
    word = input()
    arynum = int(input()) 
    tary = sys.stdin.readline().rstrip()[1:-1].split(",")
    ary = deque(tary)
    revcnt = 0    
    if arynum ==0:
        ary = deque()

    for i in word:
        if i == 'R':
            revcnt +=1
        elif i == 'D':
            if len(ary) ==0:
                print("error")
                cnt = 1
                break
            else:
                if revcnt%2!=0:
                    ary.pop()
                else:
                    ary.popleft()
    if cnt == 0:
        if revcnt%2 ==0:            
            print ("["+",".join(ary)+"]")

        else:
            ary.reverse()
            print ("["+",".join(ary)+"]")



