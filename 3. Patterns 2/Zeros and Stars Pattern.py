n = int(input())
rows = 2*n + 1
i = 1

while i <= n:
    j = 1
    while j <= rows:
        if(j == i or j == (rows // 2 + 1) or j == rows - i +1):
            print('*',end = '')
            
        else:
            print('0',end = '')

        j = j + 1
        
    print()
    i = i + 1