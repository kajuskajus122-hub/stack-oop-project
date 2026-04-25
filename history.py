"""history.py - StackHistory class demonstrating the Aggregation principle."""

from operation_record import OperationRecord


class StackHistory:
    """Records operations performed on stacks during a session.

    Aggregation principle: StackHistory holds *references* to operation
    records describing external stack events. The stacks themselves exist
    and function independently - destroying the history does not affect them.
    """

    def __init__(self):
        """Initialise an empty history log."""
        self._records: list[OperationRecord] = []

    def record(self, operation: str, stack_id: str, value=None) -> None:
        """Log a stack operation.

        Args:
            operation (str): Name of the operation ('push', 'pop', etc.).
            stack_id  (str): Label identifying which stack was used.
            value         : The value involved in the operation, if any.
        """
        self._records.append(
            OperationRecord(operation=operation, stack_id=stack_id, value=value)
        )

    def get_history(self) -> list[OperationRecord]:
        """Return a copy of all recorded operations."""
        return list(self._records)

    def filter_by_stack(self, stack_id: str) -> list[OperationRecord]:
        """Return only operations for a specific stack.

        Args:
            stack_id (str): The stack label to filter by.
        """
        return [r for r in self._records if r.stack_id == stack_id]

    def clear(self) -> None:
        """Remove all recorded history."""
        self._records.clear()

    def print_history(self) -> None:
        """Print all recorded operations to stdout."""
        if not self._records:
            print("  No operations recorded.")
            return
        for record in self._records:
            print(f"  {record}")

    def __len__(self) -> int:
        return len(self._records)

    def __repr__(self) -> str:
        return f"StackHistory({len(self._records)} records)"
