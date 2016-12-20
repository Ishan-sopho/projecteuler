f=open(r'euler 81.txt','r')
M=[]
for i in f:
    K=[]
    L=i.split(',')
    for j in L:
        K.append(int(j))
    M.append(K)
N=[]
N.append(M[0][0])
for i in range (1,80):
    T=[]
    for j in range (i+1):
        if j==0:
            T.append(M[j][i-j]+N[j])
        elif j==i:
            T.append(M[j][i-j]+N[j-1])
        else:
            if N[j]<N[j-1]:
                T.append(M[j][i-j]+N[j])
            else:
                T.append(M[j][i-j]+N[j-1])     
    N=T
for k in range (1,80):
    T=[]
    for l in range (79,k-1,-1):
             if N[79-l]<N[79-l+1]:
                 T.append(M[l][80-l]+N[79-l])
             else:
                 T.append(M[l][80-l]+N[79-l+1])
    print T
    N=T
print N


    
