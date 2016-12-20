import time
p=time.time()
t=286
def tri(n):
    return n*(n+1)/2
while True:
    T=tri(t)
    if ((1+(1+24*T)**0.5)/6.0)%1==0 and ((1+(1+8*T)**0.5)/4.0)%1==0:
        print T
        break
    t+=1
print 'time:',time.time()-p
