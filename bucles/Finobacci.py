a = 0
b = 1
for x in range(0,18,+1):
    print(a,end=" ")
    c= a+b
    a =b
    b =c

    '''
    a = 0
    b = 1
    
    0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597
    a b c
    
    c = a+b    c = 0+1 = 1
    a = b      0 = 1   a = 1
    b = c     1 = 1    b = 1
    c = a+b  1+1  c= 2
    
     
    '''