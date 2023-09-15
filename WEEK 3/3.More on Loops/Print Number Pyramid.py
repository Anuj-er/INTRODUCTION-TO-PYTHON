n = int(input())

for row in range(1, n+1):
    for space in range(1, row):
        print(' ', end='')

    for num in range(row, n+1):
        print(num, end='')
        
    print()

for row in range(n-1, 0, -1):
    for space in range(1, row):
        print(' ', end='')

    for num in range(row, n+1):
        print(num, end='')
        
    print()
