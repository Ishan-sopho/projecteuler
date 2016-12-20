def quadratic (a,b,c):
    D=b**2-4*a*c
    if D<0:
        return 'no solution'
    if D==0:
        return -b/(2*a)
    if D>0:
        return 'soln 1',(-b+D**0.5)/(2*a),'soln 2',(-b-D**0.5)/(2*a)

