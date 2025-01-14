import os
from Tree import *
from printTree import *


def parce(exp):
    stack = []
    curr = None

    for ch in exp:
        if ch == '(':
            if curr:
                stack.append(curr)
            curr = Tree(None)
        elif ch == ')':
            if stack:
                parent_node = stack.pop()
                if not parent_node.left:
                    parent_node.left = curr
                else:
                    parent_node.right = curr
                curr = parent_node
        elif ch.isdigit() or ch.isalpha():
            if not curr.value:
                curr.value = ''
            curr.value += ch
    return curr


def copy_to_avl(node, avl_node):  # центрированный обход
    # avl_node = AvlNode()
    insert(avl_node, int(node.value), node.value)
    if node.left is not None:
        copy_to_avl(node.left, avl_node)
    if node.right is not None:
        copy_to_avl(node.right, avl_node)


def parce_from_file():
    with open('derevo.txt', 'r') as file:  # чтение из файла
        s = file.read()
        #print(s)

    return parce(s)


stop = False

tree = parce_from_file()

avl_tree = AvlNode(None)
copy_to_avl(tree, avl_tree)

while not stop:
    print("Дерево, переданное из файла:")
    printTree(tree, None, None)

    print("Текущее авл дерево:")
    printTree(avl_tree, None, None)

    print("\nВыберите действие:")
    print("1. Добавить элемент", "2. Удалить элемент", "3. найти элемент",
          "4. Обход в ширину", "5. Прямой обход", "6. Центрированный обход", "7. Обратный обход",
          "8. Выход", sep='\n')

    print("Ваш выбор: ", end="")
    choice = int(input())

    if choice == 1:
        print("Введите значение:", end="")
        n = int(input())
        insert(avl_tree, n, n)
    elif choice == 2:
        print("Введите значение удаляемого элемента: ", end="")
        delete_avl(avl_tree, int(input()))
    elif choice == 3:
        print("Введите значение искомого элемента: ", end="")
        if search(avl_tree, int(input())) is not None:
            print("Элемент найден")
        else:
            print("Элемент не найден")
        os.system("pause")
    elif choice == 4:
        print("Обход в ширину: ", end="")
        avl_tree.width_walk()
        print()
        os.system("pause")
    elif choice == 5:
        print("Прямой обход: ", end="")
        avl_tree.straight_walk()
        print()
        os.system("pause")
    elif choice == 6:
        print("Центрированный обход: ", end="")
        avl_tree.centre_walk()
        print()
        os.system("pause")
    elif choice == 7:
        print("Обратный обход: ", end="")
        avl_tree.reverse_walk()
        print()
        os.system("pause")
    elif choice == 8:
        stop = True


    os.system('cls')
