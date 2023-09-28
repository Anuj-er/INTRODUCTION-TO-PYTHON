n, m = map(int, input().split())
array_2d = []
for _ in range(n):
    row = list(map(int, input().split()))
    array_2d.append(row)
for i in range(n):
    for _ in range(n - i):
        for elem in array_2d[i]:
            print(elem, end=" ")
        print()
