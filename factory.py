"""factory.py - Factory Method design pattern for creating Stack objects."""

from stack import Stack
from bounded_stack import BoundedStack
from min_stack import MinStack


class StackFactory:
    """Centralises stack creation using the Factory Method pattern.

    Instead of calling Stack(), BoundedStack(), or MinStack() directly,
    callers use StackFactory.create(stack_type, ...). This decouples
    object creation from business logic and makes adding new types easy.

    Why Factory over Singleton?
        Singleton suits a single shared instance. Here we need to create
        many different stack objects, so Factory Method is the better fit.
    """

    _SUPPORTED = ("basic", "bounded", "min")

    @staticmethod
    def create(stack_type: str, **kwargs) -> Stack:
        """Create and return a stack of the requested type.

        Args:
            stack_type (str): One of 'basic', 'bounded', or 'min'.
            **kwargs: Extra arguments forwarded to the constructor.
                      For 'bounded': max_size (int) is required.

        Returns:
            Stack: A concrete stack instance.

        Raises:
            ValueError: If stack_type is not recognised.
        """
        match stack_type.lower().strip():
            case "basic":
                return Stack()
            case "bounded":
                return BoundedStack(max_size=kwargs.get("max_size", 10))
            case "min":
                return MinStack()
            case _:
                raise ValueError(
                    f"Unknown stack type: '{stack_type}'. "
                    f"Supported: {StackFactory._SUPPORTED}"
                )

    @staticmethod
    def supported_types() -> tuple:
        """Return the tuple of supported stack type strings."""
        return StackFactory._SUPPORTED
