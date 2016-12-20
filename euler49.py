import prime_generator
L=prime_generator.prime(10000)
N=L[1000:10000]
for i in N:
    if i==0: continue
    else:
        M=sorted(str(i))
        if 0 in M: continue
        for j in N:
            if j==0 and j<i: continue
            else:
                    K=sorted(str(j))
                    if 0 in K: continue
                    elif K==M:
                        for k in N:
                            if k==0 and k<j: continue
                            else:
                                    A=sorted(str(k))
                                    if 0 in A: continue
                                    elif A==k:
                                        print i,j,k
                                        raw_input()
        
