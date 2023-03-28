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
        self.assertIsNone(linked_list.head)
        linked_list.insert_beginning({'id_test': 1})
        self.assertEqual(linked_list.head.data, {'id_test': 1})
        linked_list.insert_beginning({'id_test': 2})
        self.assertEqual(linked_list.head.data, {'id_test': 2})

    def test_insert_at_end(self):
        linked_list = LinkedList()
        self.assertIsNone(linked_list.head)
        linked_list.insert_at_end({'id_test': 1})
        self.assertEqual(linked_list.tail.data, {'id_test': 1})
        linked_list.insert_at_end({'id_test': 2})
        self.assertEqual(linked_list.tail.data, {'id_test': 2})

    def test__str__(self):
        linked_list = LinkedList()
        self.assertEqual(str(linked_list), 'None')
        linked_list.insert_beginning({'id_test': 1})
        self.assertEqual(str(linked_list), " {'id_test': 1} -> None")
        linked_list.insert_beginning({'id_test': 2})
        self.assertEqual(str(linked_list), " {'id_test': 2} -> {'id_test': 1} -> None")

    def test_to_list(self):
        linked_list = LinkedList()
        self.assertEqual(linked_list.to_list(), [])
        linked_list.insert_beginning({'id_test': 1})
        self.assertEqual(linked_list.to_list(), [{'id_test': 1}])
        linked_list.insert_beginning({'id_test': 2})
        self.assertEqual(linked_list.to_list(), [{'id_test': 2}])
