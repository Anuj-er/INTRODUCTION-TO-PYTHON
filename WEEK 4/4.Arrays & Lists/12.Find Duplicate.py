
import sys

def duplicateNumber(arr, n):
    seen = set()
    for num in arr:
        if num in seen:
            return num
        seen.add(num)
    return -1

#You need to copy the above function ^^

#Taking Input Using Fast I/O
def takeInput() :
    n = int(sys.stdin.readline().strip())

    if n == 0 :
        return list(), 0

    arr = list(map(int, sys.stdin.readline().strip().split()))
    return arr, n


#main
t = int(sys.stdin.readline().strip())

while t > 0 :
    
    arr, n = takeInput()
    print(duplicateNumber(arr, n))

    t -= 1
    