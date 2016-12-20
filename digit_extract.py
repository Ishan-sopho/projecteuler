def digext(x):
    L=[]
    while x/1!=0:
        L.insert(0,x%10)
        x/=10
    return L
        
