r,n,p,c=100,1,0,1
while r>0.10:
    c+=2
    n+=4.0
    temp,flag=0,1
    while temp<3 and flag:
        temp+=1
        m,flag=c**2-temp*(c-1),1
        for i in range (2,m/2+1):
            if m%i==0:
                flag=0
                break
        if flag:
            p+=1
    r=p/n
print c
