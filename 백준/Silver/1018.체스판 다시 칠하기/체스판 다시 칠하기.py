n, m = map(int, input().split())
chesspan = [input()for _ in range(n)]
cnt = []
for a in range(n-7):
    for b in range(m-7):
        ws = 0
        bs = 0

        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0:
                    if chesspan[i][j] !='W':
                        ws +=1
                    if chesspan[i][j] !='B':
                        bs +=1
                else:
                    if chesspan[i][j] !='B':
                        ws +=1
                    if chesspan[i][j] !='W':
                        bs +=1
        cnt.append(min(ws,bs))
print(min(cnt))