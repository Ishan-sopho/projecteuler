L=[4]
for i in range (2,101):
    for j in range (2,1001):
        tval,n=False,i**j
        for k in L:
            if k==n:
                tval=True
        if tval:
            continue
        else:
            L.append(n)
print len(L)
        
        
        
