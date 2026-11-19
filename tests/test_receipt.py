# Tests for receipt.py. Run them with: pytest (in the exercise folder, with the virtual environment on).
# Each test runs receipt.py the way `python receipt.py` does, types the answers in its name (the name for the
# order, the popcorns, then the sodas), and reads the numbered lines it prints, such as "4) subtotal: 27.00".
# A failing test says what it typed, the line it expected and the line receipt.py printed, or the error that
# stopped receipt.py.
# You don't need to change this file.
import os
import re
import subprocess
import sys
from pathlib import Path

import pytest

SCRIPT = Path(__file__).resolve().parent.parent / "receipt.py"


def typing(typed):
    """How a test's message starts: "Typing 'Maya', '3', '2', receipt.py", or just "menu.py" for a script that
    asks nothing, so the tests type nothing."""
    if not typed:
        return SCRIPT.name
    return "Typing " + ", ".join(repr(answer) for answer in typed) + ", " + SCRIPT.name


def run_script(*typed):
    """Runs the script with this Python, types each answer in typed followed by Enter, and returns what happened.
    A run still going after 10 seconds is stopped: a while loop that never ends is the usual reason."""
    __tracebackhide__ = True
    try:
        return subprocess.run(
            [sys.executable, str(SCRIPT)],
            input="".join(answer + "\n" for answer in typed),
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=10,
            env={**os.environ, "PYTHONUTF8": "1"},  # the same text on every computer
        )
    except subprocess.TimeoutExpired:
        pass  # failed below, outside this except, so pytest shows only the message
    pytest.fail(
        f"{typing(typed)} was still running after 10 seconds, so the test stopped it. Look for a while loop that "
        "never ends: does the loop change, or ask again for, the value its condition checks?",
        pytrace=False,
    )


def printed_lines(result):
    """Each line the script printed that has a line number and ")", by that number:
    "1) name: Maya" -> {"1": "1) name: Maya"}.
    When the tests type the answers, nothing ends the question's line, so a numbered line can come right after a
    question, as in "How many sodas? 1) name: Maya". The number is found there too."""
    lines = {}
    for line in result.stdout.splitlines():
        match = re.search(r"(?:^|\s)(\w+)\)", line)
        if match:
            lines[match.group(1)] = line[match.start(1):].strip()
    return lines


def expect(condition, message):
    """Fails with just the message when the condition isn't true."""
    __tracebackhide__ = True  # pytest shows the message, not this helper's code
    if not condition:
        pytest.fail(message, pytrace=False)


def program_runs(result, typed=()):
    """Fails, with the end of Python's traceback, when the script stopped with an error."""
    __tracebackhide__ = True
    traceback_end = "\n".join([line for line in result.stderr.splitlines() if line.strip()][-4:])
    same_answers = ", type the same answers," if typed else ""
    expect(
        result.returncode == 0,
        f"{typing(typed)} stopped with an error. Run python {SCRIPT.name} in the terminal{same_answers} and read "
        "the traceback from its last line up:\n" + traceback_end,
    )


def check(typed, number, expected):
    """Fails unless the script, given these answers, ran to the end and printed exactly the line expected."""
    __tracebackhide__ = True
    result = run_script(*typed)
    program_runs(result, typed)
    lines = printed_lines(result)
    expect(number in lines, f"{typing(typed)} printed no line {number}. It should print: {expected}")
    got = lines[number]
    expect(got == expected, f"{typing(typed)} should print the line: {expected}\nbut it printed: {got}")


MAYAS_ORDER = ["Maya", "3", "2"]


def test_1_name_maya_prints_as_maya():
    check(MAYAS_ORDER, "1", "1) name: Maya")


def test_2_name_typed_with_spaces_and_no_capital_prints_as_maya():
    check(["  maya  ", "3", "2"], "1", "1) name: Maya")


def test_3_popcorns_3_prints_as_3():
    check(MAYAS_ORDER, "2", "2) popcorns: 3")


def test_4_sodas_2_prints_as_2():
    check(MAYAS_ORDER, "3", "3) sodas: 2")


def test_5_subtotal_for_3_popcorns_and_2_sodas_is_27_00():
    check(MAYAS_ORDER, "4", "4) subtotal: 27.00")


def test_6_tax_for_3_popcorns_and_2_sodas_is_1_89():
    check(MAYAS_ORDER, "5", "5) tax: 1.89")


def test_7_total_for_3_popcorns_and_2_sodas_is_28_89():
    check(MAYAS_ORDER, "6", "6) total: 28.89")


def test_8_total_for_0_popcorns_and_1_soda_is_4_01():
    check(["Leo", "0", "1"], "6", "6) total: 4.01")


def test_9_tax_for_4_popcorns_and_1_soda_rounds_to_2_08():
    check(["Ana", "4", "1"], "5", "5) tax: 2.08")


def test_10_subtotal_for_10_popcorns_and_4_sodas_is_80_00():
    check(["Sam", "10", "4"], "4", "4) subtotal: 80.00")


def test_11_total_for_10_popcorns_and_4_sodas_is_85_60():
    check(["Sam", "10", "4"], "6", "6) total: 85.60")


def test_12_total_for_0_popcorns_and_0_sodas_is_0_00():
    check(["Rosa", "0", "0"], "6", "6) total: 0.00")
