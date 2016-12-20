import time
start_time = time.time()
x=1010101030
while x<1389026623 :
    l=str(x*x)
    tval,k=True,2
    for i in range (2,18,2) :
        tval=True
        if l[i]!=str(k):
            break
        else :
            k+=1
            tval=False
    if tval:
        x+=10
    else:
        print x
        break
print "My program took", time.time() - start_time, "to run"
