prime,s,i=0,600851475143,2
while i<s:
    while True:
        if s%i==0:
            s/=i
            prime=s
        else:
            i+=1
            break
print prime
    
    
