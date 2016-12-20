import time
start_time = time.time()
summ=1
L=[i for i in range (2,21)]
for j in L:
    summ*=j
    for k in range (len(L)):
        if L[k]%j==0:
            L[k]/=j
print summ  
print("--- %s seconds ---" % (time.time() - start_time))
    
        



