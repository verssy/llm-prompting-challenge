#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) != 2:
        print("usage: ./solution.py <test_XXX.in>")
        sys.exit(1)
    test_file = sys.argv[1]
    print(f"testing file = {test_file}")

if __name__ == "__main__":
    main()
