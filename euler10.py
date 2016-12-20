import time
start_time = time.time()
summ=0
L=[i for i in range (2000000)]
for j in L:
    if j>1414:
        break
    if j==0 or j==1:
        continue
    else :
        m=j*j
        while m<2000000:
            L[m]=0
            m+=j
for k in L:
    summ+=k
print summ-1
print("--- %s s ---" % (time.time() - start_time))
