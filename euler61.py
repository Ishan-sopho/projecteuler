def check(x,y):
    if y==0:
        if ((-1+(1+8*x)**0.5)/2.0)%1==0: return 1
        else: return 0
    elif y==1:
        if (x**0.5)%1==0:return 1
        else: return 0
    elif y==2:
        if ((1+(1+24*x)**0.5)/6.0)%1==0: return 1
        else: return 0
    elif y==3:
        if ((1+(1+8*x)**0.5)/4.0)%1==0: return 1
        else: return 0
    elif y==4:
        if ((3+(9+10*x)**0.5)/10.0)%1==0: return 1
        else: return 0
m,n,L=1001,19,[]
while m>1000 :
    m=n*(3*n-2)
    if m>10000: break
    if (m/10)%10!=0:
        L.append(m)
    n+=1
print L
for i in L:
    l=i
    summ=i
    for j in range(5):
        flag=0
        for k in range (10,100):
            l=(l%100)*100+k
            if check(l,j):
                flag=1
                summ+=l
                break
            else:
                summ=i
    if flag and j==4:print summ
            
                
            
            
            


        
    
