"""helpers.py - Shared CLI helper utilities used by action modules."""

import state

SEP = "=" * 50


def hdr(title: str) -> None:
    """Print a section header."""
    print(f"\n{SEP}\n  {title}\n{SEP}")


def get_stack_name() -> str | None:
    """Prompt the user to select a stack by name.

    Returns:
        str | None: The chosen stack name, or None if invalid/unavailable.
    """
    if not state.stacks:
        print("  No stacks exist yet. Create one first.")
        return None
    print("  Available:", ", ".join(state.stacks.keys()))
    name = input("  Stack name: ").strip()
    if name not in state.stacks:
        print(f"  Stack '{name}' not found.")
        return None
    return name


def parse_value(raw: str):
    """Cast raw string input to int or float where possible."""
    for cast in (int, float):
        try:
            return cast(raw)
        except ValueError:
            pass
    return raw
