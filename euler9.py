for i in range (250):
    for j in range (500):
        k=(i*i+j*j)**0.5
        if k%1==0 and i+j+k==1000:
            print i*j*k
            print i,j,k
            break
            
































        
