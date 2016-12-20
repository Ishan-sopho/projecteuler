count=0
for a in range (3):
    for b in range (5):
        for c in range (11):
            for d in range (21):
                for e in range (41):
                    for f in range (101):
                        for g in range (201):
                            summ=a*100+b*50+c*20+d*10+e*5+f*2+g*1
                            if summ==200:
                                count+=1
                                break
print count
                            
                            
                            
