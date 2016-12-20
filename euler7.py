import prime_generator
L=prime_generator.prime(1000000)
count=0
for i in L:
    if i==0: continue
    else:
        count+=1
    if count==10001:
        break
print i
