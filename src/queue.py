class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self, head=None, tail=None):
        """
        Конструктор класса Queue
        """
        self.queue = ""
        self.head = head
        self.tail = tail

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        new_node = Node(data, None)
        if self.head is None and self.tail is None:  # список пуст первый входящий узел равен началу и концу строки
            self.head = self.tail = new_node
            self.queue += str(new_node.data)
        else:
            pass

    def dequeue(self):
        """
        Метод для удаления элемента из очереди и его возвращения

        :return: данные удаленного элемента
        """
        pass

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        return f""
