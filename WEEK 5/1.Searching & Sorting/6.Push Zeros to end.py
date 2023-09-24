def pushZerosAtEnd(arr, n) :
    non_zero_index = 0
    for i in range(n):
        if arr[i] != 0:
            arr[i], arr[non_zero_index] = arr[non_zero_index], arr[i]
            non_zero_index += 1
