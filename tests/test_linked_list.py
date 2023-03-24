"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import unittest
from src.linked_list import LinkedList


class LinkedListTest(unittest.TestCase):

    def test_init(self):
        """
        Тест конструктора класса Queue
        """
        linked_list = LinkedList()
        self.assertEqual(linked_list.head, None)  # проверка начала очереди
        self.assertEqual(linked_list.tail, None)  # проверка конца очереди

    def test_insert_beginning(self):
        linked_list = LinkedList()
        linked_list.insert_beginning({'id': 1})

    def test_insert_at_end(self):
        linked_list = LinkedList()
        linked_list.insert_at_end({'id': 2})



