import datetime
import json
import os
import sys

# from https://gist.github.com/minism/1590432
class fg:
    BLACK   = '\033[30m'
    RED     = '\033[31m'
    GREEN   = '\033[32m'
    YELLOW  = '\033[33m'
    BLUE    = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN    = '\033[36m'
    WHITE   = '\033[37m'
    RESET   = '\033[39m'

class bg:
    BLACK   = '\033[40m'
    RED     = '\033[41m'
    GREEN   = '\033[42m'
    YELLOW  = '\033[43m'
    BLUE    = '\033[44m'
    MAGENTA = '\033[45m'
    CYAN    = '\033[46m'
    WHITE   = '\033[47m'
    RESET   = '\033[49m'

class style:
    BRIGHT    = '\033[1m'
    DIM       = '\033[2m'
    NORMAL    = '\033[22m'
    RESET_ALL = '\033[0m'

LOGFILE = "ecpyl_log.json"
BARKS = {
  "init" : f"""\
        +========================================+
        | {fg.BLACK + bg.BLUE + style.BRIGHT}Stop being lazy and just do some shit.{style.RESET_ALL} |
        +========================================+
""",
  "title" : "Entry title?",
  "entry" : """\

Type Ctrl+D (Ctrl+Z on Windows) on a line by itself
plus enter to finish your entry.
"""
}

def write_entry_to_file(entry):
  previous_entries = []

  if os.path.isfile(LOGFILE):
    with open(LOGFILE) as previous_log:
      previous_entries = json.load(previous_log)
  
  previous_entries.append(entry)

  with open(LOGFILE, 'w') as new_log:
    json.dump(previous_entries, new_log, indent=2)


if __name__ == "__main__":
  # https://stackoverflow.com/questions/12492810/python-how-can-i-make-the-ansi-escape-codes-to-work-also-in-windows
  os.system("") # workaround to get color to work for windows terminals

  print(BARKS["init"])

  while True:
    entry = {}

    print(fg.RED + BARKS["title"] + style.RESET_ALL, end = ' ')
    entry["title"] = input()
    entry["datetime"] = datetime.datetime.utcnow().isoformat()

    entry_header = f"Entry for \"{entry['title']}\""
    print(fg.CYAN + style.BRIGHT + BARKS["entry"] + style.RESET_ALL)
    print(fg.RED + entry_header + style.RESET_ALL)
    print("-" * len(entry_header))
    print("=" * 72)
    entry["message"] = sys.stdin.readlines()

    write_entry_to_file(entry)

    print("")
    print("=" * 72)
    print("")
