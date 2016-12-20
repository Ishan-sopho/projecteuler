sol=0
c=40000
while sol<1000:
    sol=0
    c+=1
    for i in range (2,c/2+1):
        if 1.0/(1.0/c-1.0/i)%1==0:
            sol+=1
    print sol
print c
    
    
