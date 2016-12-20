count=0
for i in range (2,1000000):
    if i%2==0:
        p=1
        while p<i:
            if i%p!=0:
                count+=1
            p+=2
    else:
        q=1
        while q<i:
            if i%q!=0:
                count+=1
            q+=1
print count
