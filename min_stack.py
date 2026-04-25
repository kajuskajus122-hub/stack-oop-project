"""min_stack.py - A Stack that tracks the minimum value in O(1) time."""

from stack import Stack


class MinStack(Stack):
    """A stack that retrieves the minimum element in O(1) time.

    Uses an auxiliary Stack internally (Composition) to track minimums.
    Overrides push and pop to maintain the tracker (Polymorphism +
    Inheritance pillars).
    """

    def __init__(self):
        """Initialise an empty MinStack with an auxiliary min-tracker."""
        super().__init__()
        self._min_tracker = Stack()     # Composition: MinStack owns this

    def push(self, value) -> None:
        """Push a value and update the minimum tracker.

        Overrides Stack.push (Polymorphism pillar).
        """
        super().push(value)
        if self._min_tracker.is_empty() or value <= self._min_tracker.peek():
            self._min_tracker.push(value)

    def pop(self):
        """Remove and return the top value, updating the min tracker.

        Overrides Stack.pop (Polymorphism pillar).

        Raises:
            IndexError: If the stack is empty.
        """
        value = super().pop()
        if value == self._min_tracker.peek():
            self._min_tracker.pop()
        return value

    def get_min(self):
        """Return the current minimum value in the stack in O(1).

        Raises:
            IndexError: If the stack is empty.
        """
        if self._min_tracker.is_empty():
            raise IndexError("MinStack is empty.")
        return self._min_tracker.peek()

    def clear(self) -> None:
        """Clear both the main stack and the min tracker."""
        super().clear()
        self._min_tracker.clear()

    def __repr__(self) -> str:
        min_val = self.get_min() if not self.is_empty() else "N/A"
        return f"MinStack({self.to_list()}, min={min_val})"
