def m(i):
    a=0
    p = -1
    for j in range(1,i+1,1):
        p = -p
        a = a+ (1/(2*j-1))*p
    return 4*a



print('i             m(i)')
for i in range(1,902,1):
    print(i, '\t\t%.4f'%m(i))
