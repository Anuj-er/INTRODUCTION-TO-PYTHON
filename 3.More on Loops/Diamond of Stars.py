n = int(input())
m = n // 2+1

for i in range(1,m+1):
    for space in range(m-i):
        print(' ', end='')
    for star in range(2 * i-1):
        print('*', end='')
    print()
for i in range(1, m):
    for space in range(i):
        print(' ', end='')
    for star in range(1,n-2 * i+1):
        print('*', end='')
    print()
