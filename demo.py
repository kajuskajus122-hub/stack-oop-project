"""demo.py - Automated demonstration of all Stack features."""

from factory import StackFactory
from file_handler import FileHandler
import state


def run_demo() -> None:
    """Automated demo so assessors can see all features at a glance."""
    sep = "=" * 50
    print(f"\n{sep}\n  Automated Demo\n{sep}")

    print("  [1/3] Basic Stack - push 10, 20, 30 then pop")
    basic = StackFactory.create("basic")
    state.stacks["demo_basic"] = basic
    for v in [10, 20, 30]:
        basic.push(v)
        state.history.record("push", "demo_basic", v)
    popped = basic.pop()
    state.history.record("pop", "demo_basic", popped)
    print(f"  Pushed 10, 20, 30  ->  {basic}  |  pop -> {popped}")

    print("\n  [2/3] BoundedStack (max=3) - overflow example")
    bounded = StackFactory.create("bounded", max_size=3)
    state.stacks["demo_bounded"] = bounded
    for v in [1, 2, 3]:
        bounded.push(v)
        state.history.record("push", "demo_bounded", v)
    print(f"  {bounded}  |  is_full={bounded.is_full}")
    try:
        bounded.push(99)
    except OverflowError as exc:
        print(f"  OverflowError caught: {exc}")

    print("\n  [3/3] MinStack - tracking minimum in O(1)")
    min_s = StackFactory.create("min")
    state.stacks["demo_min"] = min_s
    for v in [5, 3, 8, 1, 4]:
        min_s.push(v)
        state.history.record("push", "demo_min", v)
        print(f"    push({v})  ->  min={min_s.get_min()}")

    FileHandler.save_to_csv(min_s, state.CSV_FILE, "min")
    print(f"\n  MinStack saved to '{state.CSV_FILE}'.")
    print(f"  History log now contains {len(state.history)} operations.")
