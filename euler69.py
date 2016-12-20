def tot(x):
    for i in range (2,x**0.5+1):
        
        
import prime_generator
L=prime_generator.prime(1000000)
c,maxx=9,0
while c<1000:
    c+=1
    tot=1
    if L[c]==c:continue
    else:
         m=c/tot(c)
    print m
    if m>maxx:maxx=m
print maxx
                
                
    
    
        
