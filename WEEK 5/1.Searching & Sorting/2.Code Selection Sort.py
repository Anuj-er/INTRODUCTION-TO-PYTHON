from typing import List

# #Using Simple Sort() function
# def selectionSort(arr: List[int]) -> None: 
#     new_arr = arr.sort()
#     return new_arr



##Using Loops
def selectionSort(arr: List[int]) -> None: 
    for i in range (len(arr)):
        min_index = i
        for g in range(i+1,len(arr)):
            if arr[g]<arr[min_index]:
                min_index = g 
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr