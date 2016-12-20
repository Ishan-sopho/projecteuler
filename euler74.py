import factorial
c,count=69,0
def digfact(x):
    summ=0
    while x/10!=0:
        summ+=factorial.factorial(x%10)
        x/=10        
while c<1000000:
    c+=1
    rep=1
    copy=digfact(c)
    while rep<61:
        if copy==169:
            rep+=2
            if rep==60:
                count+=1
            break
        elif copy==871 or copy==872:
            rep+=1
            if rep==60:
                count+=1
            break
        copy=digfact(copy)
        rep+=1
print count
        
        
    
