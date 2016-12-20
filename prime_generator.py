def prime(x):
    L=[i for i in range (x)]
    L[1]=0
    for j in L:
        if j>x**0.5:
            break
        if j==0 :
            continue
        else :
            m=j*j
            while m<x:
                L[m]=0
                m+=j
    return L
        
