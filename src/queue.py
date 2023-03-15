class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node
        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """
        Конструктор класса Queue
        """
        self.head = None
        self.tail = None

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        if not self.head:  # отрабатывает тогда, если не существует первого элемента
            self.head = Node(data)  # создаем первый элемент
            self.tail = self.head  # так как это первый элемент, он равен и началу и концу цепи
            return data  # возврат элемента для окончания функции
        node = self.head  # если существует первый элемент
        while node.next_node:  # пока существует следующий элемент
            node = node.next_node  # постоянно присваиваем +1 элемент
        node.next_node = Node(data)
        self.tail = node.next_node  # присваиваем последний элемент хвосту
        return data

    def dequeue(self):
        """
        Метод для удаления элемента из очереди и его возвращения

        :return: данные удаленного элемента
        """
        pass

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        return f""
