from typing import List

def insertionSort(a: List[int], n: int) -> None:
    for i in range(1,len(a)):
        j = i-1
        temp = a[i]
        while (j>=0 and a[j]>temp):
            a[j+1]= a[j]
            j = j-1
        a[j+1]=temp
    return a

