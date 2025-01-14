MINIMUM = 64

import os
import random


class DArray(object):
    def make_array(self, size) -> list:
        return [None] * size

    def __init__(self, size=0):
        self.ASize = size  # элементы в массиве
        self.LSize = size + 1  # элементы в списке
        self.array = self.make_array(self.LSize)

    def __len__(self):
        return self.ASize

    def __add__(self, other):
        return other

    def __iadd__(self, other):
        plus = self.ASize
        for i in range(0, len(other)):
            self.add(other.find(i), i + plus)
        return self

    def __getitem__(self, item):
        slc = DArray()
        if isinstance(item, slice):
            if item.start is None:
                start = 0
            else:
                start = item.start
            if item.stop is None:
                stop = len(self)
            else:
                stop = item.stop
            for i in range(start, stop):
                slc.add(self.find(i), i - start)
        else:
            slc.add(self.find(item), 0)
        return slc

    def ensure_capacity(self, size: int):
        if self.LSize < size:
            self.LSize = self.ASize * 2
            new_array = self.make_array(self.LSize)
            for i in range(self.ASize):
                new_array[i] = self.array[i]
            self.array = new_array

    def add(self, element, index: int):

        if index > self.ASize + 1:
            raise ValueError

        self.ensure_capacity(self.ASize + 1)

        for i in reversed(range(index + 1, self.ASize + 1)):
            self.array[i] = self.array[i - 1]

        self.array[index] = element
        self.ASize += 1

    def remove(self, index):
        if self.ASize == 0:
            # print("Массив пуст")
            return
        if index < 0 or index >= self.ASize:
            return IndexError("Индекс слишком большой")
        if index == self.ASize - 1:
            self.array[index] = 0
            self.ASize -= 1
            return
        for i in range(index, self.ASize - 1):
            self.array[i] = self.array[i + 1]
        self.array[self.ASize - 1] = 0
        self.ASize -= 1

    def change(self, data, ind: int):
        self.array[ind] = data

    def print(self):
        for i in range(self.ASize):
            print(self.array[i], end=" ")

    def make_rand(self, size):
        arr = self.make_array(size)
        for i in range(0, size):
            arr[i] = random.randint(0, 100)
            self.array = arr
        self.ASize = size

    def copy(self, start=0, end=-1):
        if end == -1:
            end = self.ASize
        arr_cop = DArray(end - start)
        for i in range(start, end):            arr_cop.change(self.array[i], i)
        return arr_cop

    def find(self, ind):
        return self.array[ind]


def find_minrun(n):
    r = 0
    if n < MINIMUM:  # если N < 64 ТО МИНРАН = Н
        return n
    while n >= MINIMUM:
        r |= n & 1
        n >>= 1
    # print(n+r)
    return n + r


def insertion_sort(array, left, right):
    for i in range(left + 1, right + 1):
        element = array[i]
        j = i - 1
        while element < array[j] and j >= left:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = element
    return array


def merge(array, l, m, r):
    array_length1 = m - l + 1
    array_length2 = r - m
    left = []
    right = []
    for i in range(0, array_length1):
        left.append(array[l + i])
    for i in range(0, array_length2):
        right.append(array[m + 1 + i])

    i = 0
    j = 0
    k = l

    while j < array_length2 and i < array_length1:
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1

        else:
            array[k] = right[j]
            j += 1

        k += 1

    while i < array_length1:
        array[k] = left[i]
        k += 1
        i += 1

    while j < array_length2:
        array[k] = right[j]
        k += 1
        j += 1


def tim_sort(array):
    n = len(array)
    minrun = find_minrun(n)
    #print("\nMinrun: (это так для меня)", end=' ')
    #print(minrun)
    #("\n")

    for start in range(0, n, minrun):
        end = min(start + minrun - 1, n - 1)
        insertion_sort(array, start, end)

    size = minrun
    while size < n:

        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))
            merge(array, left, mid, right)

        size = 2 * size





def arr_demo():
    arr = DArray()
    ex = False
    while not ex:
        os.system('cls')

        #print(arrlen)
        print("1) Добавить элемент")
        print("2) Заполнить массив случайными числами")
        print("3) Очистить массив")
        print("4) Удалить элемент по индексу")
        print("5) Изменить элемент по индексу")
        print("6) Timsort")
        print("7) Выйти")

        print("\nМассив: ")
        arr.print()

        print("\nВыберете действие: ", end="")
        ch = int(input())

        os.system('cls')

        if ch == 1:
            print("Введите индекс:")
            ind = int(input())
            print("Введите значение элемента:")
            arr.add(input(), ind)

        elif ch == 2:
            print("Введите индекс, с которого начнется заполнение: ")
            ind = int(input())
            print("Введите количество элементов: ")
            count = int(input())
            for i in range(int(count)):
                randomelement = random.randint(0, 999)
                arr.add(randomelement, ind)

        elif ch == 3:
            arrlen = arr.__len__()
            for i in range(arrlen):
                arr.remove(0)


        elif ch == 4:
            print("Введите индекс:")
            arr.remove(int(input()))

        elif ch == 5:
            print("Введите индекс:")
            ind = int(input())
            print("Введите новое значение элемента:")
            arr.change(input(), ind)

        elif ch == 6:
            #array = [-1, 5, 0, -3, 11, 9, -2, 7, 0]

            print("Исходный массив:")
            arr.print()

            #arr.remove(int(input()))
            arrlen = arr.__len__()
            #print(arrlen)

            new_array = arr.make_array(arrlen)
            for i in range(arrlen):
                new_array[i] = arr.array[i]

            #if arrlen != 0:
            tim_sort(new_array)

            print("\nОтсортированный массив:")
            #print(new_array)
            for i in range(arrlen):
                #print(new_array[i])
                print(new_array[i], end = " ")
            print("\n")

            #for i in range(arrlen):
            #   arr.array[i] =  new_array[i]

            os.system('pause')

        else:
            ex = True

arr_demo()
