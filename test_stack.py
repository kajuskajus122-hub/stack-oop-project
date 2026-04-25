"""test_stack.py - Unit tests for the Stack project.

Run with:
    python -m unittest test_stack -v
"""

import os
import unittest

from bounded_stack import BoundedStack
from factory import StackFactory
from file_handler import FileHandler
from history import StackHistory
from min_stack import MinStack
from node import StackNode
from operation_record import OperationRecord
from stack import Stack


class TestStackNode(unittest.TestCase):

    def test_stores_value(self):
        self.assertEqual(StackNode(42).value, 42)

    def test_next_defaults_to_none(self):
        self.assertIsNone(StackNode("x").next)

    def test_next_setter(self):
        n1, n2 = StackNode(1), StackNode(2)
        n1.next = n2
        self.assertIs(n1.next, n2)

    def test_repr_contains_value(self):
        self.assertIn("7", repr(StackNode(7)))


class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()

    def test_new_stack_is_empty(self):
        self.assertTrue(self.stack.is_empty())

    def test_push_increases_size(self):
        self.stack.push(1)
        self.assertEqual(self.stack.size, 1)

    def test_pop_returns_last_pushed(self):
        self.stack.push(10)
        self.stack.push(20)
        self.assertEqual(self.stack.pop(), 20)

    def test_pop_empty_raises(self):
        with self.assertRaises(IndexError):
            self.stack.pop()

    def test_peek_does_not_remove(self):
        self.stack.push(5)
        self.stack.push(15)
        self.assertEqual(self.stack.peek(), 15)
        self.assertEqual(self.stack.size, 2)

    def test_peek_empty_raises(self):
        with self.assertRaises(IndexError):
            self.stack.peek()

    def test_clear_empties_stack(self):
        for i in range(5):
            self.stack.push(i)
        self.stack.clear()
        self.assertTrue(self.stack.is_empty())

    def test_to_list_top_first(self):
        for v in [1, 2, 3]:
            self.stack.push(v)
        self.assertEqual(self.stack.to_list(), [3, 2, 1])

    def test_lifo_order(self):
        values = [10, 20, 30, 40]
        for v in values:
            self.stack.push(v)
        result = [self.stack.pop() for _ in values]
        self.assertEqual(result, list(reversed(values)))

    def test_len_dunder(self):
        self.stack.push("a")
        self.stack.push("b")
        self.assertEqual(len(self.stack), 2)


class TestBoundedStack(unittest.TestCase):

    def setUp(self):
        self.stack = BoundedStack(max_size=3)

    def test_invalid_max_size(self):
        with self.assertRaises(ValueError):
            BoundedStack(0)

    def test_push_within_capacity(self):
        for v in [1, 2, 3]:
            self.stack.push(v)
        self.assertEqual(self.stack.size, 3)

    def test_push_over_capacity(self):
        for v in [1, 2, 3]:
            self.stack.push(v)
        with self.assertRaises(OverflowError):
            self.stack.push(4)

    def test_is_full(self):
        self.assertFalse(self.stack.is_full)
        for v in [1, 2, 3]:
            self.stack.push(v)
        self.assertTrue(self.stack.is_full)

    def test_not_full_after_pop(self):
        for v in [1, 2, 3]:
            self.stack.push(v)
        self.stack.pop()
        self.assertFalse(self.stack.is_full)

    def test_max_size_property(self):
        self.assertEqual(self.stack.max_size, 3)


class TestMinStack(unittest.TestCase):

    def setUp(self):
        self.stack = MinStack()

    def test_get_min_single(self):
        self.stack.push(5)
        self.assertEqual(self.stack.get_min(), 5)

    def test_get_min_multiple(self):
        for v in [5, 3, 8, 1, 4]:
            self.stack.push(v)
        self.assertEqual(self.stack.get_min(), 1)

    def test_get_min_updates_after_pop(self):
        self.stack.push(3)
        self.stack.push(1)
        self.stack.pop()
        self.assertEqual(self.stack.get_min(), 3)

    def test_get_min_empty_raises(self):
        with self.assertRaises(IndexError):
            self.stack.get_min()

    def test_duplicate_min(self):
        self.stack.push(2)
        self.stack.push(2)
        self.stack.pop()
        self.assertEqual(self.stack.get_min(), 2)

    def test_clear_resets_min_tracker(self):
        self.stack.push(10)
        self.stack.clear()
        with self.assertRaises(IndexError):
            self.stack.get_min()


class TestStackFactory(unittest.TestCase):

    def test_create_basic(self):
        self.assertIsInstance(StackFactory.create("basic"), Stack)

    def test_create_bounded(self):
        s = StackFactory.create("bounded", max_size=5)
        self.assertIsInstance(s, BoundedStack)
        self.assertEqual(s.max_size, 5)

    def test_create_min(self):
        self.assertIsInstance(StackFactory.create("min"), MinStack)

    def test_unknown_type_raises(self):
        with self.assertRaises(ValueError):
            StackFactory.create("queue")

    def test_case_insensitive(self):
        self.assertIsInstance(StackFactory.create("BASIC"), Stack)

    def test_supported_types(self):
        types = StackFactory.supported_types()
        for t in ("basic", "bounded", "min"):
            self.assertIn(t, types)


class TestFileHandler(unittest.TestCase):

    FILE = "test_io.csv"

    def tearDown(self):
        if os.path.exists(self.FILE):
            os.remove(self.FILE)

    def test_save_and_load_integers(self):
        s = Stack()
        for v in [10, 20, 30]:
            s.push(v)
        FileHandler.save_to_csv(s, self.FILE, "basic")
        _, values = FileHandler.load_from_csv(self.FILE)
        restored = Stack()
        for v in values:
            restored.push(v)
        self.assertEqual(restored.to_list(), [30, 20, 10])

    def test_type_label_preserved(self):
        s = Stack()
        s.push(1)
        FileHandler.save_to_csv(s, self.FILE, "bounded")
        stack_type, _ = FileHandler.load_from_csv(self.FILE)
        self.assertEqual(stack_type, "bounded")

    def test_missing_file_raises(self):
        with self.assertRaises(FileNotFoundError):
            FileHandler.load_from_csv("no_such_file.csv")

    def test_empty_stack_saves_and_loads(self):
        FileHandler.save_to_csv(Stack(), self.FILE, "basic")
        _, values = FileHandler.load_from_csv(self.FILE)
        self.assertEqual(values, [])


class TestStackHistory(unittest.TestCase):

    def setUp(self):
        self.history = StackHistory()

    def test_record_and_length(self):
        self.history.record("push", "s1", 10)
        self.assertEqual(len(self.history), 1)

    def test_filter_by_stack(self):
        self.history.record("push", "s1", 1)
        self.history.record("push", "s2", 2)
        self.history.record("pop", "s1", 1)
        self.assertEqual(len(self.history.filter_by_stack("s1")), 2)

    def test_clear(self):
        self.history.record("push", "s1", 5)
        self.history.clear()
        self.assertEqual(len(self.history), 0)

    def test_record_str(self):
        rec = OperationRecord(operation="push", stack_id="s1", value=42)
        self.assertIn("push", str(rec))
        self.assertIn("s1", str(rec))


if __name__ == "__main__":
    unittest.main(verbosity=2)
