'''You are given the following information, but you may prefer to do some research for yourself.
 •1 Jan 1900 was a Monday.
 •Thirty days has September,
 April, June and November.
 All the rest have thirty-one,
 Saving February alone,
 Which has twenty-eight, rain or shine.
 And on leap years, twenty-nine.
 •A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
 
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?'''

M=[31,28,31,30,31,30,31,31,30,31,30,31]
y,d=1901,1
days,tdays=0,0
while y<2001 :
    for i in M:
        if i==28 and (y%4==0  or y==2000):
            copy=i+1
        else :
            copy=i
        for j in (1,copy+1):
            tdays+=1
            if d==7:
                d=0
            d+=1
            if d==7 and j==1:
                days+=1
    if tdays==366 and (y%4==0  or y==2000):
        y+=1
        tdays=0
    elif d==365 and (y%4!=0  or y!=2000):
        y+=1
        tdays=0
print days

    
    
    
        
