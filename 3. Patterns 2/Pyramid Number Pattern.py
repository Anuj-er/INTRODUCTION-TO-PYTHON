n = int(input())
i = 1

while i <= n:
    sp = 1
    while sp <= n-i:
        print(' ',end ='')
        sp = sp + 1
        
    p = i
    j = 1
    
    while j <= i:
        print(p, end ='')
        p = p - 1
        j = j + 1
        
    p = 2
    while p <= i:
        print(p, end ='')
        p = p + 1
    
    print()
    i = i + 1