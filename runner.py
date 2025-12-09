#!/usr/bin/env python3
import glob
import os
import subprocess
import sys
from pathlib import Path

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RESET = "\033[0m"

def run_test(python_file, test_input, expected_output):
    try:
        result = subprocess.run(
            [sys.executable, python_file, str(Path(test_input).resolve())],
            text=True,
            capture_output=True,
            timeout=120
        )
        if result.returncode != 0:
            return False, f"failed with code: {result.returncode}: {result.stderr}"
        actual = result.stdout.rstrip('\n')
        with open(expected_output, 'r') as f:
            expected = f.read().rstrip('\n')
        if actual == expected:
            return True, "OK"
        else:
            return False, f"{YELLOW}    expected:{RESET}\n{expected}\n{YELLOW}    actual:{RESET}\n{actual}"
    except subprocess.TimeoutExpired:
        return False, "timout (120 seconds)"
    except FileNotFoundError:
        return False, f"not found: {python_file}"
    except Exception as e:
        return False, f"error: {str(e)}"

def main():
    if len(sys.argv) != 3:
        print("usage: ./runner.py <python_file> <tests_directory>")
        sys.exit(1)
    python_file = sys.argv[1]
    tests_dir = sys.argv[2]
    if not os.path.exists(python_file):
        print(f"error: file '{python_file}' not found")
        sys.exit(1)
    if not os.path.exists(tests_dir):
        print(f"error: directori '{tests_dir}' not found")
        sys.exit(1)
    test_files = sorted(glob.glob(os.path.join(tests_dir, "test_*.in")))
    if not test_files:
        print(f"error: not found test files in directory '{tests_dir}'")
        sys.exit(1)
    print(f"running tests for: {python_file} ...")
    print("-" * 42)
    passed = 0
    failed = 0
    for test_input in test_files:
        test_name = os.path.basename(test_input).replace('.in', '')
        expected_output = test_input.replace('.in', '.out')
        if not os.path.exists(expected_output):
            print(f"{test_name}: skipped - {expected_output} not found")
            continue
        print(f"{test_name}: ", end="", flush=True)
        success, message = run_test(python_file, test_input, expected_output)
        if success:
            print(f"{GREEN}[PASS  ]{RESET}")
            passed += 1
        else:
            print(f"{RED}[  FAIL]{RESET}")
            print(f"{message}")
            failed += 1
    print("-" * 42)
    print(f"Results: {passed} passed, {failed} failed")
    if failed > 0:
        sys.exit(1)

if __name__ == "__main__":
    main()
