"""node.py - StackNode class used for building Stack via composition."""


class StackNode:
    """Represents a single node in a linked-list-based stack.

    Each node holds a value and a reference to the next node.
    Stack is composed of these nodes (Composition principle).
    """

    def __init__(self, value):
        """Initialise a node with a value and no next link.

        Args:
            value: The data stored in this node.
        """
        self._value = value
        self._next = None

    @property
    def value(self):
        """Return the node's stored value."""
        return self._value

    @property
    def next(self):
        """Return the next node in the chain."""
        return self._next

    @next.setter
    def next(self, node):
        """Set the next node.

        Args:
            node (StackNode | None): Node to link to.
        """
        self._next = node

    def __repr__(self):
        return f"StackNode({self._value!r})"
