def check(x):
    while x/1!=0:
        if (x%10)%2==0:return 0
        x/=10
    return 1
c,count,L=10,0,[]
while c<1000000000:
    c+=1
    if c in L:continue
    if c%10==0:continue
    s=str(c)
    if (int(s[0])%2==0 and int(s[-1])%2==0) or (int(s[0])%2!=0 and int(s[-1])%2!=0):continue
    n=int(s[::-1])
    if check(c+n):
        count+=2
        L.append(n)
print count
    
    
