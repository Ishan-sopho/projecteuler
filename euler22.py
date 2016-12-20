import time
start_time = time.time()
f,N,temp=open('euler 22.txt'),[],''
L=f.read().split(',')
L.sort()
summ=0
for k in range (len(L)):
    psumm=0
    for j in range (1,len(L[k])-1):
        psumm+=ord(L[k][j])-64
    summ+=psumm*(k+1)
print summ
print("--- %s seconds ---" % (time.time() - start_time))
    


