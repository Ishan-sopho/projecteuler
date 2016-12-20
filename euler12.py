import prime_generator
L=prime_generator.prime(30000)
i,j,div=1,1,1
while div<500:
    i+=1
    j+=i
    if j>10:
        div,n=1,j**0.5
        for k in L:
            t=1
            if k==0: continue
            while k<n:
                if j%k==0:
                    t+=1
                    j/=k
            div*=t
            print t
        div+=2
        print div
print j
    
    
