a = int(input())
left, right = 1, 1
while(1):    
    if left*right >= a:
        print(left, right)
        break
    if left >= right:
        right += 1
    else:
        left += 1

        
