tval,i=True,1
def digit (x):
    L=[]
    for j in str(x):
        L.append(int(j))
        L.sort()
    return L
while tval:
    m=[]
    m.append(i)
    for k in range(2,7):
        ttval=True
        if digit(i)!=digit(i*k):
            ttval=False
        if not ttval:
            i+=1
        else:
            tval=False
print i
            
            
        
        
