summ=0
for i in range (1000,1000000):
    flag=1
    s=str(i)
    n=len(s)
    for j in range(n/2):
        if s[j]!=s[n-j]:
            flag=0
            break
    if flag:
        b=bin(i)
        m=len(b)
        for k in range(m/2):
            if b[k]!=b[m-k]:
                flag=0
                break
    if flag:
        summ+=i
print summ
