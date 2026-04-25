"""state.py - Shared mutable state for the interactive CLI.

Keeping shared objects here avoids passing them as arguments through
every function and prevents circular imports between actions and demo.
"""

from history import StackHistory

stacks: dict = {}           # name -> Stack instance
history: StackHistory = StackHistory()
CSV_FILE: str = "stack_state.csv"
