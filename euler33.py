L=[]
while len(L)<8:
    for i in range (1,10):
        for j in range (1,10):
            for k in range (1,10):
                if j==k: continue
                if j/float(k)==10*i+j/10.0*i+k:
                    L.append(10*i+j)
                    L.append(10.0*i+k)
                    break
                if j/float(k)==10*j+i/10.0*k+i:
                    L.append(10*j+i)
                    L.append(10.0*k+i)
                    break
                if j/float(k)==10*i+j/10.0*k+i:
                    L.append(10*i+j)
                    L.append(10.0*k+i)
                    break
                if j/float(k)==10*j+i/10.0*i+k:
                    L.append(10*j+i)
                    L.append(10.0*i+k)
                    break
