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

        if type(other) is not DArray:
            return self.add(other)

        res = self
        res += other
        return res

    def __iadd__(self, other):
        if type(other) is not DArray:
            self.add(other)
            return self

        plus = self.ASize
        for i in range(0, len(other)):
            self.add(other.find(i), i + plus)

        return self

    def __repr__(self):
        self.print()
        return ''

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

            return slc
        else:
            return self.find(item)

    def __setitem__(self, key=-1, value=None):
        if key == -1:
            key = self.ASize - 1

        if key >= self.ASize:
            self.add(value)
        else:
            self.change(value, key)

    def ensure_capacity(self, size: int):
        if self.LSize < size:
            self.LSize = self.ASize * 2
            new_array = self.make_array(self.LSize)

            for i in range(self.ASize):
                new_array[i] = self.array[i]

            self.array = new_array

    def add(self, element, index=-1):
        if index == -1:
            index = self.ASize

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
            print(self.array[i], end='')
        print()

    def copy(self, start=0, end=-1):
        if end == -1:
            end = self.ASize

        arr_cop = DArray(end - start)

        for i in range(start, end):
            arr_cop.change(self.array[i], i)

        return arr_cop

    def find(self, ind):
        if ind == -1:
            ind = self.ASize-1

        return self.array[ind]



def split(s, sym=' '):
    res = DArray()
    s = s + sym
    temp = ''

    for i in s:
        if i == sym and temp != '':
            res += temp
            temp = ''
        elif i != sym:
            temp += i


    return res
