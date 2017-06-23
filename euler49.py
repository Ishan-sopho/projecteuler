import prime_generator
L=prime_generator.prime(10000)
M, N= [], []
def perm_check(check1, check2):
    for i in check1:
        if check1.count(i) != check2.count(i):
            return 0
    return 1
for i in L[1000:10000]:
    if i != 0 :
        flag = False
        for j in str(i):
            if j == '0':
                flag = True
                break
        if flag:
            continue
        N.append(i)
possible = []
for i in range(len(N)):
    for j in range(i+1, len(N)):
        if N[j]+N[j]-N[i] > 10000:
            break
        if perm_check(str(N[i]), str(N[j])) and N[j]+N[j]-N[i] in N \
                and perm_check(str(N[i]), str(N[j]+N[j]-N[i])):
            possible.append((N[i], N[j], N[j]+N[j]-N[i]))

print ''.join([str(i) for i in possible[1]])
#     if i==0: continue
#     else:
#         M=sorted(str(i))
#         if 0 in M: continue
#         for j in N:
#             if j==0 and j<i: continue
#             else:
#                     K=sorted(str(j))
#                     if 0 in K: continue
#                     elif K==M:
#                         for k in N:
#                             if k==0 and k<j: continue
#                             else:
#                                     A=sorted(str(k))
#                                     if 0 in A: continue
#                                     elif A==k:
#                                         print i,j,k
#                                         raw_input()
