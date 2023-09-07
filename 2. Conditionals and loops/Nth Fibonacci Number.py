n = int(input())
if n == 1:
    print(1)
elif n == 2:
    print(1)
else:
    first = 0
    second = 1
    count = 3
    while count <= n+1:
        new = first + second
        first = second
        second = new
        count = count + 1
    print(second)