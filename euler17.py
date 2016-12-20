U=[0,3,3,5,4,4,3,5,5,4]
T=[6,6,5,5,5,7,6,6]
t=[3,6,6,8,8,7,7,9,8,8]
summ=11
for i in range(1,1000):
    psum,tval,L=0,False,[0,0,0]
    for j in range(len(str(i))):
        L[j]=(i%10)
        i/=10
    if L[1]==1:
        psum+=t[L[0]]
    else:
        psum+=U[L[0]]
        if L[1]!=0:
            psum+=T[L[1]-2]
    if L[2]==0:
        continue
    else:
        psum+=10+U[L[0]]
    summ+=psum
print summ
    

    
        
    
    
        
    
        
    
