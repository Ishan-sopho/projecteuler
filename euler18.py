import time
start_time = time.time()
f=open(r'euler 18.txt','r')
M=[]
for i in f:
    M.append(i.split())
N=[]
N.append(int(M[0][0]))
for i in range (1,len(M)):
    T=[]
    for j in range (len(M[i])):
        if j==0:
            T.append(int(M[i][j])+N[j])
        elif j==len(M[i])-1:
            T.append(int(M[i][j])+N[j-1])
        else:
            if N[j]>N[j-1]:
                T.append(int(M[i][j])+N[j])
            else:
                T.append(int(M[i][j])+N[j-1])     
    N=T
print max(N)
print("--- %s seconds ---" % (time.time() - start_time))
