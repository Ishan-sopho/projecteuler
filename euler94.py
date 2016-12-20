S=0
i=4
while i<7 :
    x=(((i+1)*(4*i**2-i-1))**0.5)*0.25
    print x
    if x//1==x:
        S+=3*i+1
    i+=1
print S
    
