g=0
for i in range (10,1001):
    count=0
    for m in range (1,int(i/2)):
        if ((i-m**2)/float(m))%1==0:
            count+=1
        if count>g:
            g=count
print g
