import time
start_time = time.time()
f=open(r'euler 67.txt','r')
M=[]
for i in f:
    M.append(i.split())
N=[]
for k in M[len(M)-1]:
    N.append(int(k))
for i in range (len(M)-2,-1,-1):
    T=[]
    for j in range (len(M[i])):
             if N[j]>N[j+1]:
                 T.append(int(M[i][j])+N[j])
             else:
                 T.append(int(M[i][j])+N[j+1])
                
    N=T
print max(N)
print("--- %s seconds ---" % (time.time() - start_time))
