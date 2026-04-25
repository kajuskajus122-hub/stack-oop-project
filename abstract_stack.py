"""abstract_stack.py - Abstract base class defining the Stack interface."""

from abc import ABC, abstractmethod


class AbstractStack(ABC):
    """Defines the contract every stack must fulfil (Abstraction pillar).

    Any concrete stack must implement push, pop, peek, and is_empty.
    Because AbstractStack cannot be instantiated directly, forgetting
    to implement any method raises a TypeError at runtime.
    """

    @abstractmethod
    def push(self, value) -> None:
        """Push a value onto the top of the stack."""

    @abstractmethod
    def pop(self):
        """Remove and return the top value of the stack."""

    @abstractmethod
    def peek(self):
        """Return the top value without removing it."""

    @abstractmethod
    def is_empty(self) -> bool:
        """Return True if the stack contains no elements."""
