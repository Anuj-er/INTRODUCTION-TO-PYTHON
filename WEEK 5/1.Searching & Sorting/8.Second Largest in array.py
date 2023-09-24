from sys import stdin


MIN_VALUE = -2147483648 
def secondLargestElement(arr, n):
    if n == 0 : 
        return MIN_VALUE
    largest = arr[0] 
    secondLargest = MIN_VALUE 
    for i in range(n) : 
        if largest < arr[i] : 
            secondLargest = largest 
            largest = arr[i]
        elif secondLargest < arr[i] and arr[i] != largest :
            secondLargest = arr[i] 
    return secondLargest 
    



def takeInput() :
    n = int(stdin.readline().rstrip())
    if n != 0:
        arr = list(map(int, stdin.readline().rstrip().split(" ")))
        return arr, n

    return list(), 0


#main
arr, n = takeInput()
print(secondLargestElement(arr, n))
