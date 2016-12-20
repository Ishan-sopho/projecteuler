'''An irrational decimal fraction is created by concatenating the positive integers:
 
0.123456789101112131415161718192021...
 
It can be seen that the 12th digit of the fractional part is 1.
 
If dn represents the nth digit of the fractional part, find the value of the following expression.
 
d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000'''
i,count,n,p=0,0,10,1
while True :
    i+=1
    l=len(str(i))
    count+=l
    if count>=n:
        d=l-(count-n)-1
        p*=int(str(i)[d])
        n*=10
        if n>1000000:
            break
print p
        
    
    
    
    
    
