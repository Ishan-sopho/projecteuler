def palchk(s):
    x=str(s)
    n=len(x)
    for i in range (n/2+1):
        if x[i]!=x[n-1-i]:
            return 0
    return 1

        
        
    
