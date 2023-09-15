N = int(input())
i = 1

while i <= N:
    j = 1
    while j <= i:
        if j == 1 or j == i:
            print("1", end="")
        else:
            print("2", end="")
        j += 1
    print()
    i += 1