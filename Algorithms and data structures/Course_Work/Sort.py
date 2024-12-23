from DArray import *

def ins_sort(arr, start=0, end=-1):

    if end == -1:
        end = len(arr)

    for j in range(start, end):
        val = arr[j][2]
        i = j - 1
        while i >= start and arr[i][2] > val:
            arr[i+1], arr[i] = arr[i], arr[i+1]
            i -= 1