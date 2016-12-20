count=2
summ=322
h=273
while count<12:
    h+=2
    b=h+1/2
    l=(h**2+b**2)**0.5
    if l%1==0:
        summ+=l
        count+=1
        continue
    b=h-1/2
    m=(h**2+b**2)**0.5
    if m%1==0:
        summ+=m
        count+=1
print summ
        
    
    
