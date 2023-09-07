n = int(input())
i = 1
while i <= n:
    space = 1
    while space <= n - i:
        print(" ", end="")
        space += 1
    number = 1
    while number <= i:
        print( number, end="")
        number += 1
    print()
    i += 1
