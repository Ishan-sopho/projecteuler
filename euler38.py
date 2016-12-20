import time
start_time = time.time()
import digit_extract
m=0
for i in range (9000,9500):
    c,s,L,flag,j=0,'',[],1,i
    while c<2 and flag:
        c+=1
        M=digit_extract.digext(j)
        for k in M:
            if k==0 or k in L:
                flag=0
                break
            else:
                L.append(k)
        if flag:
            s+=str(j)
        j+=i
    if flag and m<int(s):
        m=int(s)
print m
print("--- %s s ---" % (time.time() - start_time))
        
        
