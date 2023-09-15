n = int(input())
i = 1
while i <= n:
    space = 1
    while space <= n - i:
        print(" ", end="")
        space += 1
    
    star = 1
    while star <= i:
        print("*", end="")
        star += 1
    
    # Decreasing stars
    star = 1
    while star < i:
        print("*", end="")
        star += 1

    print()
    i += 1
