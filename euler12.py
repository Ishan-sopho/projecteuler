import time
s = time.time()

import prime_generator
L=prime_generator.prime(30000,1)
n,i=10,0
while True:
    totalcount=1
    if n%2==0:
        even,odd=n/2,n+1
    else:
        even,odd=(n+1)/2,n
    limit = odd ** 0.5
    for i in L:
        tempcount=0
        if i > limit:
            break
        while even%i==0:
            even/=i
            tempcount+=1
        while odd%i==0:
            odd/=i
            tempcount+=1
        totalcount*=(tempcount+1)
    if totalcount>500:
        print n*(n+1)/2
        print n
        break
    n+=1

t = time.time()
print(t-s)