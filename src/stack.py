from typing import Any


class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс для стека"""

    def __init__(self, top=None):
        """Конструктор класса Stack"""
        self.top = top

    def push(self, data):
        """
        Метод для последовательного добавления данных в стэк
        """
        new_node = Node(data)
        new_node.next_node = self.top
        self.top = new_node

    def pop(self):
        """
        Метод для последовательного удаления данных из стэка
        """
        remove_last = self.top
        self.top = self.top.next_node
        return remove_last.data

