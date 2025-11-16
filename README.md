# filesearch

**filesearch** is a lightweight custom CLI tool for quickly locating files by keyword.  

---

## Usage
```bash
fs [-h] [--path PATH] [--case-sensitive] [--first] keyword
```
keyword: Text to match inside filenames.

--path PATH: Directory to search. Defaults to your home directory.

--case-sensitive: Use exact-case matching. Default is case-insensitive.

--first: Stop after the first hit.

-h, --help: Show help.

> Press Ctrl+C to stop the search at any time.

## Examples

Search your home directory for any filenames containing "foo":
```bash
fs foo
```
Case-sensitive search:
```bash
fs foo --case-sensitive
```
Search the Downloads folder and stop at the first match:
```bash
fs foo --first --path C:\Users\<username>\Downloads
```

## Installation

Install the fs command globally:
```bash
pip install .
```