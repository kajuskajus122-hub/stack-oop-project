"""file_handler.py - Save and load stack state using CSV files."""

import csv
import os


class FileHandler:
    """Handles CSV serialisation and deserialisation of Stack objects.

    CSV format:
        type,value
        basic,30
        basic,20
        basic,10
    Elements are stored top-to-bottom and reversed on load so the
    original stack order is faithfully restored.
    """

    @staticmethod
    def save_to_csv(stack, filename: str, stack_type: str = "basic") -> None:
        """Save the current stack contents to a CSV file.

        Args:
            stack      : A Stack (or subclass) instance to persist.
            filename   (str): Path of the CSV file to write.
            stack_type (str): Type label stored in the file.

        Raises:
            IOError: If the file cannot be written.
        """
        with open(filename, mode="w", newline="", encoding="utf-8") as fh:
            writer = csv.writer(fh)
            writer.writerow(["type", "value"])
            for element in stack.to_list():     # top -> bottom
                writer.writerow([stack_type, element])

    @staticmethod
    def load_from_csv(filename: str) -> tuple[str, list]:
        """Load stack contents from a CSV file.

        Args:
            filename (str): Path of the CSV file to read.

        Returns:
            tuple[str, list]: (stack_type, values) where values are ordered
                bottom-to-top, ready to push in sequence.

        Raises:
            FileNotFoundError: If filename does not exist.
        """
        if not os.path.exists(filename):
            raise FileNotFoundError(f"File not found: '{filename}'")

        elements, stack_type = [], "basic"

        with open(filename, mode="r", newline="", encoding="utf-8") as fh:
            for row in csv.DictReader(fh):
                stack_type = row["type"]
                raw = row["value"]
                try:
                    elements.append(int(raw))
                except ValueError:
                    try:
                        elements.append(float(raw))
                    except ValueError:
                        elements.append(raw)

        elements.reverse()      # restore bottom-to-top push order
        return stack_type, elements
