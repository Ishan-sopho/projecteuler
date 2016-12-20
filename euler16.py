'''215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
 
What is the sum of the digits of the number 21000?'''
n=2**1000
summ=0
for i in range (len(str(n))):
    summ+=n%10
    n/=10
    print summ
