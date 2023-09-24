n = int(input())

for i in range(1, n+1):
    
    for j in range(1, n-i+2):        
        if(i%2 != 0):
            print('1', end ='')
            
        else:
            print('0', end ='')
    
    print()