from typing import List
# # This is a not Optimised Version of Bubble_Sort
# def bubbleSort(arr: List[int], n: int):
#     for i in range(len(arr)):
#         for j in range(len(arr)-1):
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1]=arr[j+1],arr[j]
#     return arr


# This is an Optimised Version of Bubble_Sort
def bubbleSort(arr: List[int], n: int):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr