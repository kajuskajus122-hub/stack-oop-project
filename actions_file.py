"""actions_file.py - CLI actions for file I/O and history display."""

from factory import StackFactory
from file_handler import FileHandler
from helpers import hdr, get_stack_name
import state

TYPE_MAP = {"Stack": "basic", "BoundedStack": "bounded", "MinStack": "min"}


def save_to_file() -> None:
    hdr("Save to CSV")
    if (name := get_stack_name()) is None:
        return
    stack_type = TYPE_MAP.get(type(state.stacks[name]).__name__, "basic")
    filename = input(f"  Filename [{state.CSV_FILE}]: ").strip() or state.CSV_FILE
    FileHandler.save_to_csv(state.stacks[name], filename, stack_type)
    state.history.record("save", name)
    print(f"  '{name}' saved to '{filename}'.")


def load_from_file() -> None:
    hdr("Load from CSV")
    filename = input(f"  Filename [{state.CSV_FILE}]: ").strip() or state.CSV_FILE
    name = input("  Name for restored stack: ").strip()
    if not name:
        print("  Name cannot be empty.")
        return
    try:
        stack_type, values = FileHandler.load_from_csv(filename)
        restored = StackFactory.create(stack_type)
        for v in values:
            restored.push(v)
        state.stacks[name] = restored
        state.history.record("load", name)
        print(f"  Loaded {len(values)} element(s) into '{name}'  ->  {restored}")
    except (FileNotFoundError, ValueError) as exc:
        print(f"  Error: {exc}")


def show_history() -> None:
    hdr("Operation History")
    print(f"  Total operations: {len(state.history)}\n")
    if not state.history.get_history():
        print("  No operations recorded yet.")
        return
    state.history.print_history()
