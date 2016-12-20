import time
t_ = time.clock()
f=open(r'euler 11.txt','r')
M=[]
for i in f:
    N=[]
    n=i.split(' ')
    for j in n:
        N.append(int(j))
    M.append(N) 
maxx=0
for k in range (20):
    for l in range (17):
        pro=1
        pro=M[k][l]*M[k][l+1]*M[k][l+2]*M[k][l+3]
        if pro>maxx:
            maxx=pro
for m in range (17):
    for n in range (20):
        pro=1
        pro=M[m][n]*M[m+1][n]*M[m+2][n]*M[m+3][n]
        if pro>maxx:
            maxx=pro
for o in range (17):
    for p in range (17):
        pro=1
        pro=M[o][p]*M[o+1][p+1]*M[o+2][p+2]*M[o+3][p+3]
        if pro>maxx:
            maxx=pro
for q in range (17):
    for r in range (3,20):
        pro=1
        pro=M[q][r]*M[q+1][r-1]*M[q+2][r-2]*M[q+3][r-3]
        if pro>maxx:
            maxx=pro
print maxx
print ('Time taken = ', time.clock() - t_,' seconds.')
    


        
