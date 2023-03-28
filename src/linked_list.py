from typing import Any


class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node
        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class LinkedList:
    """Класс для односвязного списка"""

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        node = Node(data)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next_node = node
            self.tail = node

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        return ll_string

    def to_list(self) -> list:
        """
        Метод возвращает список с данными, содержащимися в односвязном списке
        """
        lst = []
        while self.head is not None:
            lst.append(self.head.data)
            self.head = self.head.next_node
        return lst

    def get_data_by_id(self, id_value) -> Node:
        """
        Метод возвращает первый найденный словарь с ключом 'id', значение которого равно переданному в метод значению.
        """
        lst = self.to_list()
        for node in lst:
            try:
                if node['id'] == id_value:
                    return node
            except TypeError:
                print('Данные не являются словарем или в словаре нет id')

