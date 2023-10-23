import sys

filename = "test_1.py"

with open(filename, "rb") as f:
    b = f.read()

try:
    b.decode("UTF-8")
except UnicodeDecodeError:
    sys.exit(0)
else:
    raise AssertionError(
        f"{filename} must NOT be valid UTF-8. "
        "This is an error you don't want in this repo."
    )

s = b.decode("cp1252")
assert "ñ" in s, f"Did not find an 'ñ' in {filename}, even though it really should have"
