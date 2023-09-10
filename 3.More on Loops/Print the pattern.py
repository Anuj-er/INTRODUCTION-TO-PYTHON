n = int(input())

if n % 2 == 0:
    middle = n // 2
else:
    middle = n // 2 + 1

for i in range(1, middle + 1):
    for j in range(1, n + 1):
        print(2 * n * (i - 1) + j, end=' ')
    print()

remaining = n - middle
for i in range(remaining, 0, -1):
    for j in range(1, n + 1):
        print((2 * i - 1) * n + j, end=' ')
    print()
