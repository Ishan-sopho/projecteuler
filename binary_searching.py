L=[]
while True :
    n=raw_input('enter an number or break to exit:'))
    if n==break :
        break
    else :
        L+=int(n)
L.sort
""binary searching""
num=int(raw_input('enter the number you want to search'))
lo,hi=0,len(L)-1
while hi>=lo :
    x=(hi+lo)/2
    if L[x]>num :
        hi=x-1
    elif L[x]<num :
        lo=x
    elif L[x]==num :
        print 'the value is at position',x
        break
    
    
        
    
        
    
                    
