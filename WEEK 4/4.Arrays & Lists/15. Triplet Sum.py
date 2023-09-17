
from sys import stdin

def findTriplet(arr, n, x) :
    numTriplets = 0 
    for i in range(n) : 
        for j in range((i + 1), n) :
            for k in range((j + 1), n) : 
                if (arr[i] + arr[j] + arr[k]) == x :
                    numTriplets += 1 
    return numTriplets 
# You need to copy above Function ^^



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
    print(findTriplet(arr, n, x))
    t -= 1