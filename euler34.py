import factorial
def digfac(x):
    summ=0
    while x%10!=0:
        summ+=factorial.factorial(x%10)
        x/=10
    return summ
g=0
for i in range (11,100000):
    if digfac(i)==i:
        g+=i
        print i
print g
        
