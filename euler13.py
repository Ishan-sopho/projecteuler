'''work out the first ten digits of the sum of the one-hundred 50 digit numbers stored in 'euler 13.txt''''
f=open('euler 13.txt')
summ=0
for line in f:
    n=int(line)
    summ+=n
l=len(str(summ))
print summ/(10**(l-10))
