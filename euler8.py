'''The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.
Find the thirteen adjacent digits in the 1000-digit number stored in 'euler 8.txt' that have the greatest product. What is the value of this product?'''
f=open('euler 8.txt')
L,pmax=[],0
for line in f:
    L.append(str(line))
n=1000/len(L)
for i in range(989):
    p=1
    for j in range (13):
        k=(i+j)/n
        p*=int(L[k-1][(i+j)%n])
    if p>pmax:
        pmax=p
print pmax
        
    
