def ninjaPuzzle(n):
    for i in range(1, n + 1):
        for sp in range(1, i):
            print(' ', end='')
        for j in range(1, n - i + 2):
            print('*', end='')
        print()
    return 0

#DO NOT PASTE THIS
n = int(input("Enter the value of n: "))
ninjaPuzzle(n)
