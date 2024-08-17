import subprocess
import pyperclip
import sys
import json

from typing import List

from simple_term_menu import TerminalMenu


def main(keyword: str, file_name: str = "help.json", extra_arg=None) -> None:
    options = _options(keyword, file_name, extra_arg)

    terminal_menu = TerminalMenu(options, search_key=None)
    menu_entry_index = terminal_menu.show()
    if menu_entry_index is not None:
        pyperclip.copy(options[menu_entry_index])
        print(f"You have copied {options[menu_entry_index]}!")


def _options(keyword: str, file_name: str, extra_arg: str) -> List[str]:
    with open(file_name, "r") as json_file:
        helps = json.load(json_file)["helps"]
        for item in helps:
            if keyword == item["keyword"]:
                type = item["type"]
                if type == "list":
                    return item[type]
                elif type == "command":
                    command_arg = item[type]
                    if extra_arg:
                        command_arg = command_arg.replace("${1}", extra_arg)
                    commands = command_arg.split(" ")
                    result = subprocess.run(commands, stdout=subprocess.PIPE, text=True)
                    # Split the output by newlines to create a list
                    output = result.stdout.split("\n")
                    # Remove any empty strings from the list (e.g., the last element if there's a trailing newline)
                    return [line for line in output if line]

        raise ValueError(f"Unknown option, {keyword}")


if __name__ == "__main__":
    if len(sys.argv) <= 2:
        print("Specify file_name, keyword and/or additional argument")
        exit(1)

    extra_arg = None if len(sys.argv) == 3 else sys.argv[3]

    main(keyword=sys.argv[2], file_name=sys.argv[1], extra_arg=extra_arg)
