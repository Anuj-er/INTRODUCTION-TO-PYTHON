n = int(input()) 
i = 1  

while i <= n:
    space = n - i
    while space > 0:
        print(" ", end="")
        space -= 1

    j = i
    while j < 2 * i:
        print(j, end="")
        j += 1
        
    j = 2 * i - 2
    while j >= i:
        print(j, end="")
        j -= 1

    print()

    i += 1
