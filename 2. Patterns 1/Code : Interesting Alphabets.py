l = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
num = int(input())
c = num
i = 1
while i <= num:
    j = 0
    while j < i:
        print(l[c + j - 1], end="")
        j += 1
    c = c - 1
    print()
    i += 1