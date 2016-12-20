import time
start_time=time.time()
num=21780.0
count=19602.0
ratio=0
def bouncychk(x):
    flag,b=0,0
    while True:
        a=x%10
        x/=10
        b=x%10
        if a<b:
            flag=1
            break
        elif a>b:
            flag=2
            break
        else :
            if x/10==0:
                return 0
    while True:
        x/=10
        c=x%10
        if flag==1 and c<b:
            return 1
        elif flag==2 and c>b:
            return 1
        elif x/10==0:
            return 0
        b=c
while ratio!=0.9900000 :
    num+=1
    if bouncychk(num):
        count+=1
    ratio=count/num
print num,ratio
print "My program took", time.time() - start_time, "to run"


    
