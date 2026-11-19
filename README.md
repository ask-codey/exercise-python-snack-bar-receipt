# Exercise: Snack Bar Receipt

Exercise code for the lesson **Exercise: Snack Bar Receipt** in the Python in Depth course on [ask-codey.com](https://www.ask-codey.com).

The snack bar at Starlight Cinema needs a receipt for every order. `receipt.py` already asks for the customer's name and how many popcorns and sodas they want. You'll turn the answers into numbers, work out the subtotal, the tax and the total, and print the receipt as six numbered lines. The tests run your script, type the answers in for you, and check each line it prints.

## What's here

- `receipt.py`: the prices, the tax rate and the three questions, and a comment that shows the receipt to print. For you to finish.
- `tests/test_receipt.py`: tests that run `receipt.py`, type the answers in, and check the numbered lines it prints. You don't need to change this file.
- `requirements.txt`: the one package the tests need, pytest, at an exact version. Ready to use.
- `pytest.ini`: tells pytest where the tests are. Ready to use.
- `.gitignore`: tells Git to leave out the virtual environment and the files Python and pytest make as they run. Ready to use.

## Before you start

The tests need pytest, and pytest goes in a virtual environment: a private set of packages for this folder only. In VS Code's terminal, in this folder, run these three commands.

On Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

On a Mac (zsh):

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

- The first command makes the virtual environment, in a folder named `.venv`.
- The second turns it on for this terminal: the prompt starts with `(.venv)` from then on.
- The third installs the packages `requirements.txt` lists into it: here, only pytest.

*Virtual Environments and pip*, in Module 3, explains all three. The `.venv` folder is in `.gitignore`, so Git leaves it out: these commands make it again on any computer.

If PowerShell answers that running scripts is disabled on this system, run this once, then run the second command again:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

Each new terminal starts with the virtual environment off. If the prompt doesn't start with `(.venv)`, run the second command again. (VS Code often turns it on for you.)

## What to print

After the three questions, `receipt.py` prints an empty line, then the receipt: six lines, each a number, a closing parenthesis, a name and a value. Typing `Maya`, `3` and `2`, the receipt is:

```text
1) name: Maya
2) popcorns: 3
3) sodas: 2
4) subtotal: 27.00
5) tax: 1.89
6) total: 28.89
```

## The rules

- Popcorn is $6.50, a soda is $3.75, and the sales tax is 7%: use the variables `popcorn_price`, `soda_price` and `tax_rate` at the top of `receipt.py`.
- **name:** the name as typed, without the spaces around it and with a capital first letter. Typing `"  maya  "` prints `Maya`.
- **popcorns** and **sodas:** the numbers typed, as whole numbers: `3` prints as `3`.
- **subtotal:** the popcorns times the popcorn price, plus the sodas times the soda price.
- **tax:** the subtotal times the tax rate, rounded to cents with `round(..., 2)`.
- **total:** the subtotal plus the tax.
- The subtotal, the tax and the total each show exactly two decimal places: `27.00`, `1.89`, `28.89`.
- Print the six lines exactly as above: the number and a closing parenthesis, a space, the name, a colon and a space, then the value. The tests read only these six lines.
- Keep the three questions as they are, in their order, and the `print()` after them, which ends the last question's line: the tests type the answers in that order and read each numbered line from its start. Don't change the tests.

The tests type these orders, and check these lines:

| Typed | Lines checked |
|---|---|
| `Maya`, `3`, `2` | every line: `Maya`, `3`, `2`, `27.00`, `1.89`, `28.89` |
| `"  maya  "`, `3`, `2` | `1) name: Maya` |
| `Leo`, `0`, `1` | `6) total: 4.01` |
| `Ana`, `4`, `1` | `5) tax: 2.08` |
| `Sam`, `10`, `4` | `4) subtotal: 80.00` and `6) total: 85.60` |
| `Rosa`, `0`, `0` | `6) total: 0.00` |

## Check your work

```bash
pytest
```

At first every test fails: that is expected, because `receipt.py` doesn't print a receipt yet. Each line you print correctly turns its tests green. A failing test's message says what it typed, the line it expected and what came back, for example:

```text
Typing 'Maya', '3', '2', receipt.py should print the line: 4) subtotal: 27.00
but it printed: 4) subtotal: 27.0
```

To try it yourself, run it and type the answers:

```bash
python receipt.py
```

## Tips

- Work one order through by hand first: 3 popcorns at $6.50 and 2 sodas at $3.75 make 19.50 + 7.50, which is 27.00. 7% of that is 1.89, so the total is 28.89.
- `input()` always gives back text, so `popcorns` and `sodas` start out as text. `int()` turns each into a whole number before the math.
- `strip()` takes the spaces off the name, and `title()` gives it a capital first letter.
- `round(number, 2)` rounds to cents, and `{number:.2f}` in an f-string shows two decimal places, such as `27.00`.
- An f-string builds each line: `f"1) name: {name}"` is the first one.

## Hand it in

When it works, push your solution to a public repo of your own on GitHub, then paste that repo's address into **Submit your exercise** on the lesson page at [ask-codey.com](https://www.ask-codey.com). That's what completes the lesson. The lesson page shows the Git commands, step by step.
