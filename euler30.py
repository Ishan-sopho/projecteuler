count=2
def summchk(x):
    summ=0
    while x!=0:
        summ+=(x%10)**5
        x/=10
    return summ
grand=0
while count<1000000:
    if count==summchk(count):
        grand+=count
    count+=1
print grand
    
