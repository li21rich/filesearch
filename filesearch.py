import os
from pathlib import Path
import argparse

from pathlib import Path
import argparse

def main():
    parser = argparse.ArgumentParser(
        prog="fs",
        description="Search filenames by keyword"
    )
    parser.add_argument("keyword", help="Keyword to look for in filenames")
    parser.add_argument("--path", default=str(Path.home()), 
                        help="Directory to search (default: your home folder)")
    args = parser.parse_args()

    base = Path(args.path)
    keyword = args.keyword.lower()

    success = False
    for p in base.rglob("*"):
        try:
            if keyword in p.name.lower():
                print(p)
                success = True
        except PermissionError:
            continue

    if success == False:
        print(f"No matches for '{args.keyword}' in {base}")
