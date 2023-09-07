n = int(input())
i = 1

while i <= n:
    j = 0
    x = i - 1

    while j < i:
        if x == 0:
            print(1, end="")
        else:
            if x == j or j == 0:
                print(x, end="")
            else:
                print(0, end="")
        j += 1
    print()
    i += 1