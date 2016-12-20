import palindrome_check
maxx=0
for i in range (800,1000):
    for j in range (800,1000):
        if palindrome_check.palchk(i*j):
            if i*j>maxx:
                maxx=i*j
print maxx
        
        
