from pathlib import Path
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(
        prog="fs",
        description="Search filenames by keyword"
    )
    parser.add_argument("keyword", help="Keyword to look for in filenames")
    parser.add_argument("--path", default=str(Path.home()), 
                        help="Directory to search (default: your home folder)")
    parser.add_argument("--case-sensitive", action="store_true",
                        help="Make search case-sensitive (default: case-insensitive)")
    parser.add_argument("--first", action="store_true",
                        help="Stop after the first match")
    args = parser.parse_args()

    base = Path(args.path)

    if not base.exists():
        print(f"Path not found: {base}")
        sys.exit(1)

    print(f"Searching in: {base}")

    keyword = args.keyword
    matches = []

    try:
        for p in base.rglob("*"):
            try:
                name = p.name
                name_to_check = name if args.case_sensitive else name.lower()
                search_term = keyword if args.case_sensitive else keyword.lower()

                if search_term in name_to_check:
                    print(p)
                    matches.append(p)
                    if args.first:
                        break
            except PermissionError:
                continue
    except KeyboardInterrupt:
        print("\nSearch interrupted via keyboard interrupt.")
        sys.exit(1)

    if not matches:
        print(f"No matches for '{keyword}' in {base}")
        sys.exit(1)

if __name__ == "__main__":
    main()