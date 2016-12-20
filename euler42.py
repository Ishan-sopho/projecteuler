import time
t=time.time()
f=open('euler 42.txt')
L,N,count=f.read().split(','),[],0
for k in range (len(L)):
    psumm=0
    for j in range (1,len(L[k])-1):
        psumm+=ord(L[k][j])-64
    k=((1+8*psumm)**0.5-1)/0.5
    if k%1==0:
        count+=1
print count
print 'time:',time.time()-t
        

    
