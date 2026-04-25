"""main.py - Entry point and menu loop for the Stack project.

Run with:
    python main.py
"""

import actions_stack as stk
import actions_file as fil
from demo import run_demo

MENU = """
  [1] Create stack    [5] List all stacks   [9] Show history
  [2] Push            [6] Save to CSV       [d] Run demo
  [3] Pop             [7] Load from CSV     [0] Exit
  [4] Peek / Inspect  [8] Clear stack
"""

ACTION_MAP = {
    "1": stk.create_stack,
    "2": stk.push_value,
    "3": stk.pop_value,
    "4": stk.inspect_stack,
    "5": stk.list_all_stacks,
    "6": fil.save_to_file,
    "7": fil.load_from_file,
    "8": stk.clear_stack,
    "9": fil.show_history,
    "d": run_demo,
}


def main() -> None:
    print("\n  +------------------------------------+")
    print("  |    Stack Project - Main Menu       |")
    print("  +------------------------------------+")

    while True:
        print(MENU)
        choice = input("  Choice: ").strip().lower()

        if choice == "0":
            print("\n  Goodbye!\n")
            break

        action = ACTION_MAP.get(choice)
        if action:
            action()
            input("\n  Press Enter to continue...")
        else:
            print("  Unknown option. Please try again.")


if __name__ == "__main__":
    main()
