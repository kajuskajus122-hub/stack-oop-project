"""stack.py - General-purpose LIFO Stack built from StackNode objects."""

from abstract_stack import AbstractStack
from node import StackNode


class Stack(AbstractStack):
    """A Last-In, First-Out (LIFO) data structure.

    Built from StackNode objects (Composition).
    Private attributes are exposed only through controlled properties
    and methods (Encapsulation pillar).
    """

    def __init__(self):
        self._top = None    # private: head node
        self._size = 0      # private: element count

    @property
    def size(self) -> int:
        """Return the number of elements (read-only)."""
        return self._size

    def push(self, value) -> None:
        """Push a value onto the stack."""
        node = StackNode(value)
        node.next = self._top
        self._top = node
        self._size += 1

    def pop(self):
        """Remove and return the top value.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Pop from an empty stack.")
        value = self._top.value
        self._top = self._top.next
        self._size -= 1
        return value

    def peek(self):
        """Return the top value without removing it.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Peek at an empty stack.")
        return self._top.value

    def is_empty(self) -> bool:
        """Return True if the stack has no elements."""
        return self._top is None

    def clear(self) -> None:
        """Remove all elements from the stack."""
        self._top = None
        self._size = 0

    def to_list(self) -> list:
        """Return all elements as a list, top first."""
        result, current = [], self._top
        while current:
            result.append(current.value)
            current = current.next
        return result

    def __len__(self) -> int:
        return self._size

    def __repr__(self) -> str:
        return f"Stack({self.to_list()})"
