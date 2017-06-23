numer,denom=1,1
def multiply(i,j,k,num,dum):
    num*=j
    dum*=k
    print i,j,k
    return num,dum
for i in range (1,10):
    for j in range (10):
        for k in range(j+1,10):
            if i==j or i==k:
                continue
            if float(str(i)+str(j))/float(str(i)+str(k))==float(j)/float(k):
                numer,denom=multiply(i,j,k,numer,denom)
                continue
            elif float(str(j)+str(i))/float(str(k)+str(i))==float(j)/float(k):
                numer, denom = multiply(i, j, k,numer, denom)
                continue
            if j<i:
                if float(str(j)+str(i))/float(str(i)+str(k))==float(j)/float(k):
                    numer, denom = multiply(i, j, k,numer, denom)
                    continue
            elif k>i:
                if float(str(i)+str(j))/float(str(k)+str(i))==float(j)/float(k):
                    numer, denom = multiply(i, j, k,numer, denom)
                    continue
print numer,"/",denom
