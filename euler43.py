N=[0,1,2,3,4,5,6,7,8,9]
M=['0','1','2','3','4','5','6','7','8','9']
C=[2,3,5,7,11,13,17]
summ,c=0,0
while c<10:
    s,n,c='',[],0
    for i in N:
        if i not in n:
            s+=str(i)
            n.append(i)
            c+=1
        if c>3:
            if int(s[c-3:c])%C[c-4]:
                continue
            else:
                break
    if len(s)==10 and sorted(s)==M:
        summ+=int(s)
print summ
        
            
        
        
    
