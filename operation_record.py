"""operation_record.py - Dataclass for a single recorded stack operation."""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Optional


@dataclass
class OperationRecord:
    """Stores details of a single stack operation.

    Used by StackHistory to build an audit log of everything that
    happened across all active stacks during a session.
    """

    operation: str              # e.g. 'push', 'pop', 'peek'
    stack_id: str               # label of the stack involved
    value: Optional[Any] = None # value involved, if any
    timestamp: str = field(
        default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )

    def __str__(self) -> str:
        val_str = f", value={self.value!r}" if self.value is not None else ""
        return (
            f"[{self.timestamp}] {self.stack_id}: "
            f"{self.operation}{val_str}"
        )
