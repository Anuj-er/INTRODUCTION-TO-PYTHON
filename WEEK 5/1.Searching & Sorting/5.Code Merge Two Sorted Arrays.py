from sys import stdin

def merge(arr1, n, arr2, m) : 
    i,j = 0,0
    len1 ,len2 = len(arr1),len(arr2)
    new_array = []
    while (i<len1 and j<len2):
        if arr1[i]<arr2[j]:
            new_array.append(arr1[i])
            i = i+1
        else:
            new_array.append(arr2[j])
            j = j+1
    while (i<len1):
        new_array.append(arr1[i])
        i = i+1
    while (j<len2):
        new_array.append(arr2[j])
        j = j+1
    
    return new_array









#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n != 0:
        arr = list(map(int, stdin.readline().rstrip().split(" ")))
        return arr, n

    return list(), 0


#to print the array/list
def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
        
    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    arr1, n = takeInput()
    arr2, m = takeInput()

    ans = merge(arr1, n, arr2, m)
    printList(ans, (n + m))

    t -= 1