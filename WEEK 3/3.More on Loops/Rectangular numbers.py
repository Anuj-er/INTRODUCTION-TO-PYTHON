n = int(input())

for i in range(1, n + 1):
    for up in range(1, i):
        print(n - up + 1, end='')

    for j in range(i, 2 * n - i + 1):
        print(n - i + 1, end='')

    for low in range(2 * n - i, 2 * n - 1):
        print(low - n + 2, end='')

    print()

for i in range(n - 1, 0, -1):
    for up in range(1, i):
        print(n - up + 1, end='')

    for j in range(i, 2 * n - i + 1):
        print(n - i + 1, end='')

    for low in range(2 * n - i, 2 * n - 1):
        print(low - n + 2, end='')

    print()

