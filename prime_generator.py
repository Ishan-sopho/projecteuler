def prime(x,type=0):
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
    if type==0:
        return L
    elif type==1:
        M=[]
        for i in L:
            if i!=0:
                M.append(i)
        return M