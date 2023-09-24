a = int(input())

k = 1
while k <= a:
    b = '1'
    i = 2
    while i <= a:
        c = str(i)
        if k >= i:
            b = b + c
        else:
            b = b + ' '
        i += 1
    j = a
    while j >= 1:
        d = str(j)
        if k >= j:
            b = b + d
        else:
            b = b + ' '
        j -= 1
    print(b)
    k += 1
