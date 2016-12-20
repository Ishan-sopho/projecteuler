'''A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.
 
Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?'''

maxx=0
for i in range (1,100):
    for j in range (1,100):
        n=len(str(i**j))
        num=i**j
        summ=0
        for k in range (1,n+1):
            l=num%10
            num=num/10
            summ+=l
        if maxx<summ :
            maxx=summ
print maxx
            
