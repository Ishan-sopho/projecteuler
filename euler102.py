def dist (a,b,x=0,y=0):
    return ((a-x)**2+(b-y)**2)**0.5
f1=open(r'euler 102.txt','r')
count=0
for line in f1:
    M,N=(line.rstrip()).split(','),[]
    for i in M:
        N.append(int(i))
    y,z,x=dist(N[0],N[1]),dist(N[2],N[3]),dist(N[4],N[5])
    if y<dist(N[0],N[1],N[2],N[3]) and y<dist(N[0],N[1],N[4],N[5]):
        if z<dist(N[0],N[1],N[2],N[3]) and z<dist(N[2],N[3],N[4],N[5]):
            if x<dist(N[0],N[1],N[4],N[5]) and x<dist(N[2],N[3],N[4],N[5]):
                count+=1           
print count
        
    
                     
