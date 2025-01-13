# двусвязный список, динамический массив и стек.
# Стек можно реализовать как на базе списка, так и отдельно.

# двусвязный список

import ctypes

class Node:
    def __init__(self, data=None):
        self.item = data
        self.prev = None  # предыдущий узел
        self.next = None  # следующий узел


class DoublyLinkedList:
    def __init__(self):
        self.start = None  # определяем переменную для начала списка

    def find(self, index) -> Node:
        current = self.start
        while index > 0:
            index -= 1
            current = current.next
        return current

    def size(self) -> int:
        count = 0
        current = self.start
        while current is not None:
            count += 1
            current = current.next
        return count

    def add(self, element: str, index: int):
        new_node = Node()
        new_node.item = element

        if index > self.size():
            #print("Неверный индекс")
            return

        if index == 0:
            new_node.next = self.start
            self.start = new_node
        else:
            prev_node = self.find(index - 1)
            new_node.next = prev_node.next
            new_node.prev = prev_node
            prev_node.next = new_node

    def remove(self, index: int):
        if index == 0:
            self.start = self.start.next
            self.start.next.prev = None
        else:
            prev_node = self.find(index - 1)
            prev_node.next = prev_node.next.next
            if index != self.size():
                prev_node.next.prev = prev_node

    def change(self, index: int, data):
        temp_node = self.find(index)
        temp_node.item = data

    def print(self):
        current = self.start
        while current.next is not None:
            print(current.item, end=" ")
            current = current.next
        print(" ")


# динамический массив

class DArray(object):

    def make_array(self, size) -> list:
        return [None] * size

    def __init__(self):
        self.ASize = 0  # элементы в массиве
        self.LSize = 1  # элементы в списке
        self.array = self.make_array(self.LSize)

    def __len__(self):
        return self.ASize

    def ensure_capacity(self, size: int):
        if self.__len__() < size:
            new_array = self.make_array(len(self.array) * 2)

            for i in range(self.ASize):
                new_array[i] = self.array[i]

            self.array = new_array

    def add(self, element: str, index: int):
        if index > self.__len__() + 1:
            raise ValueError
        self.ensure_capacity(self.__len__() + 1)
        for i in reversed(range(index + 1, self.__len__() + 1)):
            self.array[i] = self.array[i - 1]
        self.array[index] = element
        self.ASize += 1

    def print(self):
        for i in range(self.__len__()):
            print(self.array[i], end=" ")
        print()


list1 = DoublyLinkedList()
array1 = DArray()

for i in range(0, 10):
    list1.add(str(i), i)
    array1.add(str(i), i)

list1.print()

array1.print()


