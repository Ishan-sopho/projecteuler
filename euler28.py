import time
t0 = time.time()
summ,c,n,d=1,0,1,2
while c<500:
    c+=1
    p=0
    while p<4:
        p+=1
        n+=d
        summ+=n
    d+=2
print summ
t1 = time.time()
print t1-t0
