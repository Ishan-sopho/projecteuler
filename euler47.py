num=646
def primefact(x):
    count,i=0,2
    while i<x:
        flag=0
        while True:
            if x%i==0:
                x/=i
                flag=1
            else:
                if flag:
                    count+=1
                i+=1
                flag=0
                break
    return count
        
    
while True:
    num+=1
    if primefact(num)==4:
        num+=1
        if primefact(num)==4:
            num+=1
            if primefact(num)==4:
                num+=1
                if primefact(num)==4:
                    print num-3
                    break
        
    
