def factorial (x,y=1):
    if x==0 or x==1:
        return 1
    result=1
    while x>y :
        result*=x
        x-=1
    return result
        
