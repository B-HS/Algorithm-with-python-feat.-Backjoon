otsuri = 1000 - int(input())
harai = 1000
nannko = 0
while(1):
    if otsuri ==0:
        break
    
    if otsuri>=500:
        otsuri-=500
        nannko+=1
    elif otsuri>=100:
        otsuri-=100
        nannko+=1
    elif otsuri>=50:
        otsuri-=50
        nannko+=1
    
    elif otsuri>=10:
        otsuri-=10
        nannko+=1
        
    elif otsuri>=5:
        otsuri-=5
        nannko+=1
    elif otsuri>=1:
        otsuri-=1
        nannko+=1
print (nannko)
        