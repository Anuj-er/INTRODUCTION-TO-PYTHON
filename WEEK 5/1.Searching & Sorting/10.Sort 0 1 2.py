def sort012(arr, n) :
    nextZero = 0
    nextTwo = (n - 1) 
    i = 0 
    while i <= nextTwo :
        if arr[i] == 0 :
            temp = arr[nextZero]
            arr[nextZero] = arr[i] 
            arr[i] = temp
            i += 1
            nextZero += 1
        elif arr[i] == 2 :
            temp = arr[nextTwo] 
            arr[nextTwo] = arr[i] 
            arr[i] = temp
            nextTwo -= 1
        else : 
            i += 1 