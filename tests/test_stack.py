"""Здесь надо написать тесты с использованием unittest для модуля stack."""
from src.stack import Stack
import unittest


class TestStack(unittest.TestCase):
    """
    Тесты для класса Stack.
    """
    def test_init(self):
        """
        Тест конструктора класса Stack.
        """
        stack = Stack()
        self.assertIsNone(stack.top)

    def test_push(self):
        """
        Тест для добавления элемента на вершину стека.
        """
        stack = Stack()
        self.assertIsNone(stack.top)
        stack.push("test")
        self.assertEqual(stack.top.data, "test")

    def test_pop(self):
        """
        Тест для удаления элемента c вершины стека
        """
        stack = Stack()
        stack.push("test")
        self.assertEqual(stack.top.data, "test")
        stack.pop()

    def test__str__(self):
        stack = Stack()
        self.assertIsNone(stack.top)




