[[[list() for i in range(10)] for j in range (10)] for k in range(10)]

count,n=1,0
temp=None
def extandsqr(x):
    summ=0
    for i in range (len(str(x))):
        summ+=(x%10)**2
        x/=10
    if summ==89:
        n+=1
        return 1
    elif summ==1:
        return 1
    if extandsqr(summ):
        return
while count<10000000:
    extandsqr(count)
    count+=1
print n
    
    
