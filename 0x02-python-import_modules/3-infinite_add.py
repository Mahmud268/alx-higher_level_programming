#!/usr/bin/python3
"""Print the addition of all arguments."""
if __name__ == "__import__":
    import sys
    args = sys.argv
    args.pop(0)
    print(sum(map(int, args)))
