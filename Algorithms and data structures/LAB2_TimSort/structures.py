import random


class DArray(object):

    def make_array(self, size) -> list:
        return [None] * size

    def __init__(self, size=0):
        self.ASize = size  # элементы в массиве
        self.LSize = size+1  # элементы в списке
        self.array = self.make_array(self.LSize)

    def __len__(self):
        return self.ASize

    def __add__(self, other):
        return other

    def __iadd__(self, other):
        plus = self.ASize
        for i in range(0, len(other)):
            self.add(other.find(i), i+plus)

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
                slc.add(self.find(i), i-start)

            return slc
        else:
            return self.find(item)

    def ensure_capacity(self, size: int):
        if self.LSize < size:
            self.LSize = self.ASize * 2
            new_array = self.make_array(self.LSize)

            for i in range(self.ASize):
                new_array[i] = self.array[i]

            self.array = new_array

    def add(self, element, index = -1):
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
            print(self.array[i], end=" ")
        print()

    def make_rand(self, size, min = -10000, max = 10000):
        arr = self.make_array(size)
        for i in range(0, size):
            arr[i] = random.randint(min, max)
        self.array = arr
        self.ASize = size

    def copy(self, start=0, end=-1):
        if end == -1:
            end = self.ASize

        arr_cop = DArray(end - start)

        for i in range(start, end):
            arr_cop.change(self.array[i], i)

        return arr_cop

    def find(self, ind):
        return self.array[ind]





