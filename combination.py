import factorial
def combination(i,j):
    return factorial.factorial(i,i-j)/factorial.factorial(i-j)
