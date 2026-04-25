"""bounded_stack.py - A Stack with a fixed maximum capacity."""

from stack import Stack


class BoundedStack(Stack):
    """A stack that enforces a maximum number of elements.

    Inherits all behaviour from Stack and overrides push to enforce
    a size limit (Inheritance + Polymorphism pillars).
    """

    def __init__(self, max_size: int):
        """Initialise a bounded stack.

        Args:
            max_size (int): Maximum number of elements allowed.

        Raises:
            ValueError: If max_size is not a positive integer.
        """
        if max_size <= 0:
            raise ValueError("max_size must be a positive integer.")
        super().__init__()
        self._max_size = max_size   # private, encapsulated

    @property
    def max_size(self) -> int:
        """Return the maximum capacity (read-only)."""
        return self._max_size

    @property
    def is_full(self) -> bool:
        """Return True if the stack has reached its capacity."""
        return self._size >= self._max_size

    def push(self, value) -> None:
        """Push a value, raising OverflowError if the stack is full.

        Overrides Stack.push (Polymorphism pillar).

        Raises:
            OverflowError: If the stack is at maximum capacity.
        """
        if self.is_full:
            raise OverflowError(
                f"BoundedStack is full (max_size={self._max_size})."
            )
        super().push(value)

    def __repr__(self) -> str:
        return f"BoundedStack({self.to_list()}, max_size={self._max_size})"
