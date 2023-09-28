def find_leaders(arr):
    n = len(arr)
    leaders = []
    max_right = arr[n - 1] 

    for i in range(n - 1, -1, -1):
        if arr[i] >= max_right:
            leaders.append(arr[i])
            max_right = arr[i] 

    leaders.reverse()
    return leaders

n = int(input())
arr = list(map(int, input().split()))
leaders = find_leaders(arr)
print(*leaders)  