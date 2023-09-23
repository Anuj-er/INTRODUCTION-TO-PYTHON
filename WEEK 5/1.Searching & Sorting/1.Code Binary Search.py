def search(nums: [int], target: int):
    length = len(nums)
    for i in range (0,length):
        if arr[i]==target:
            return i
            break
    return -1

n= int (input())
arr = list(map(int,input().strip().split()))[:n]
target =int (input())
print (search(arr, target))