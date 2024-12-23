class Stack(object):

    def __init__(self):
        self.stack = list()

    def __len__(self):
        return len(self.stack)

    def isEmpty(self):
        return self.stack == []

    def push(self, element):  # добавляем
        self.stack.append(element)

    def pop(self):  # удаляем
        if not self.isEmpty():
            return self.stack.pop()
        #else:
            #print("Ошибка! Стек пуст")  # raise ValueError("Стек пуст")

    def get_value(self):
        if not self.isEmpty():
            return self.stack[-1]
        else:
            return ''

    def print(self):
         for i in range(len(self.stack)):
             print(self.stack[i], end = " ")