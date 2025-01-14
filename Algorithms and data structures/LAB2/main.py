from structures import *
import os

def get_minrun(n: int):
    r = 0
    while n >= 64:
        r |= (n & 1)
        n >>= 1
    return n+r


def ins_sort(arr, start=0, end=-1):

    if end == -1:
        end = len(arr)

    for j in range(start, end):
        val = arr.array[j]
        i = j - 1
        while i >= start and arr.array[i] > val:
            arr.array[i+1] = arr.array[i]
            arr.array[i] = val
            i -= 1


def merge(arr1, arr2):
    c = DArray()
    lnum, rnum = 0, 0
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        if arr1.find(i) < arr2.find(j):
            c.add(arr1[i])
            i += 1
            rnum = 0
            lnum += 1
            if lnum >= 7 and i < len(arr1):
                ind = binary_search(arr1, arr1[i], i, len(arr1)-1)
                while i < ind:
                    c.add(arr1[i])
                    i += 1

        else:
            c.add(arr2[j])
            j += 1
            lnum = 0
            rnum += 1
            if rnum >= 7 and i < len(arr2):
                ind = binary_search(arr2, arr2[i], j, len(arr2)-1)
                while j < ind:
                    c.add(arr2[j])
                    j += 1

    if i < len(arr1):
        c += arr1[i:]
    else:
        c += arr2[j:]

    return c


def merge_sort(arr):
    if len(arr) == 1:
        return arr

    middle = len(arr)//2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])

    return merge(left, right)

def binary_search(the_array, item, start, end):
    if the_array[start] is None:
        print("ggg")

    if start == end:
        if the_array[start] > item:
            return start
        else:
            return start + 1
    if start > end:
        return start

    mid = (start + end) // 2



    if the_array[mid] < item:
        return binary_search(the_array, item, mid + 1, end)

    elif the_array[mid] > item:
        return binary_search(the_array, item, start, mid - 1)

    else:
        return mid


def tim_sort(arr):
    runs, sorted_runs = DArray(), DArray()
    length = len(arr)
    min_run = get_minrun(length)

    for start in range(0, length, min_run):
        end = min(start + min_run, length)
        runs.add(arr[start: end], len(runs))
        ins_sort(runs[len(runs)-1])

    sorted = DArray()
    for i in range(len(runs)):
        sorted = merge(sorted, runs[i])

    return sorted


array = DArray()

stop = False

while not stop:
    os.system("cls")
    print("1. Timsort", "2. Выход", sep='\n', end='\n\n')
    print("Ваш выбор: ", end='')

    choice = int(input())

    os.system('cls')

    if choice == 1:
        print("Выберите размер массива: ", end='')
        array.make_rand(int(input()), -100, 100)
        os.system('cls')
        print("Исходный массив: ", array, sep='\n')

        array = tim_sort(array)

        print("Отсортированный массив: ", array, sep='\n')
        os.system("pause")
    if choice == 2:
        stop = True



