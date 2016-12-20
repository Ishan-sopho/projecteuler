import time
p=time.time()
import prime_generator
def check(x):
    summ=1
    for j in range (2,x/2+1):
        if x%j==0:
            summ+=j
    return summ
N=prime_generator.prime(100001)
req,i,K=0,11,[]
while i<10000:
    i+=1
    if i in K: continue
    if N[i]==i: continue
    new=check(i)
    K.append(new)
    if check(new)==i and new!=i:
        req+=new+i
        print new,i
print req
print 'time:',time.time()-p

    
    
    
    
