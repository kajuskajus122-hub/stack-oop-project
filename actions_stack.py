"""actions_stack.py - CLI actions for creating and operating on stacks."""

from bounded_stack import BoundedStack
from factory import StackFactory
from helpers import hdr, get_stack_name, parse_value
from min_stack import MinStack
import state


def create_stack() -> None:
    hdr("Create a Stack")
    print("  Types: basic | bounded | min")
    stack_type = input("  Choose type: ").strip().lower()
    name = input("  Stack name: ").strip()
    if not name or name in state.stacks:
        print("  Invalid or duplicate name.")
        return
    try:
        if stack_type == "bounded":
            max_size = int(input("  Max size: ").strip())
            state.stacks[name] = StackFactory.create("bounded", max_size=max_size)
        else:
            state.stacks[name] = StackFactory.create(stack_type)
        print(f"  Created {stack_type} stack '{name}'.")
    except (ValueError, KeyError) as exc:
        print(f"  Error: {exc}")


def push_value() -> None:
    hdr("Push")
    if (name := get_stack_name()) is None:
        return
    value = parse_value(input("  Value to push: ").strip())
    try:
        state.stacks[name].push(value)
        state.history.record("push", name, value)
        print(f"  Pushed {value!r}  ->  {state.stacks[name]}")
    except OverflowError as exc:
        print(f"  OverflowError: {exc}")


def pop_value() -> None:
    hdr("Pop")
    if (name := get_stack_name()) is None:
        return
    try:
        value = state.stacks[name].pop()
        state.history.record("pop", name, value)
        print(f"  Popped: {value!r}  ->  {state.stacks[name]}")
    except IndexError as exc:
        print(f"  IndexError: {exc}")


def peek_value() -> None:
    hdr("Peek")
    if (name := get_stack_name()) is None:
        return
    try:
        value = state.stacks[name].peek()
        state.history.record("peek", name, value)
        print(f"  Top of '{name}': {value!r}")
    except IndexError as exc:
        print(f"  IndexError: {exc}")


def inspect_stack() -> None:
    hdr("Inspect Stack")
    if (name := get_stack_name()) is None:
        return
    s = state.stacks[name]
    print(f"  Name    : {name}")
    print(f"  Type    : {type(s).__name__}")
    print(f"  Size    : {s.size}  |  Empty: {s.is_empty()}")
    print(f"  Content : {s.to_list()}  (top -> bottom)")
    if isinstance(s, MinStack) and not s.is_empty():
        print(f"  Minimum : {s.get_min()}")
    if isinstance(s, BoundedStack):
        print(f"  Max Cap : {s.max_size}  |  Full: {s.is_full}")


def list_all_stacks() -> None:
    hdr("All Active Stacks")
    if not state.stacks:
        print("  No stacks exist yet.")
        return
    for name, s in state.stacks.items():
        print(f"  [{name}]  {type(s).__name__:<14} size={s.size}  {s.to_list()}")


def clear_stack() -> None:
    hdr("Clear Stack")
    if (name := get_stack_name()) is None:
        return
    state.stacks[name].clear()
    state.history.record("clear", name)
    print(f"  Stack '{name}' cleared.")
