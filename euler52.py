count=125874
def digitext(x):
    L=[]
    for i in str(x):
        L.append(i)
    return list(set(L))
while True:
    count+=1
    M=digitext(count)
    if M==digitext(count*2):
        if M==digitext(count*3):
            if M==digitext(count*4):
                if M==digitext(count*5):
                    if M==digitext(count*6):
                        print count
                        break
    
