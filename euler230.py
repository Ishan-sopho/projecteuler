a,b='14159265358979323846264338327950288419716939937510\
58209749445923078164062862089986280348253421170679','82148086513282306647093844609550582231725359408128\
48111745028410270193852110555964462294895493038196'
def val(n):
    return (127+19*n)*(7**n)
def string ():
    l,m,c='p','q',''
    while True :
        c=l+m
        l=m
        m=c
        yield c
summ=0
let=string()
y=next(let)
for i in range (18):
    tval=True
    x=val(i)
    while tval :
        if len(y)*100/x>=1 :
            tval=False
            r=x%100
            if y[len(y)-1]=='p':
                summ+=10**i*(int(a[r]))
            else :
                summ+=10**i*(int(b[r]))
        else:
            y=next(let)
print summ
                
