def printTable(s, e, w):
    while True:
        c = 0
        if s <= e:
            c = (s - 32) * 5 / 9
            print(s, int(c))
            s = s + w

        else:
            break

s = int(input())
e = int(input())
step = int(input())
printTable(s, e, step)