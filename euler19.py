month=[11,12,1,2,3,4,5,6,7,8,9,10]
day,yr,cent=1,1,19
sundays=0

def days(y,c,m,d=1):
    return d+((13*m-1)/5)+y+(y/4)+(c/4)-2*c
while yr<100:
    for i in month:
        if (days(yr,cent,i))%7==0:
            sundays+=1
    yr+=1
yr,cent=0,20
for i in month:
    if (days(yr,cent,i))%7==0:
        sundays+=1
print sundays