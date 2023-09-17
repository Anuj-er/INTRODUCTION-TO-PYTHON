
from sys import stdin


def pairSum(arr, n, x) :
    element_count = {}
    pair_count = 0

    for num in arr:
        diff = x - num
        if diff in element_count:
            pair_count += element_count[diff]

        if num in element_count:
            element_count[num] += 1
        else:
            element_count[num] = 1

    return pair_count

# You need to copy above function ^^
#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().strip())
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


#main
t = int(stdin.readline().strip())

while t > 0 :
    
    arr, n = takeInput()
    x = int(stdin.readline().strip())
    print(pairSum(arr, n, x))

    t -= 1