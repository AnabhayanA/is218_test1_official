# Test 1 Specification and Rubric

## Required outcome

Fork `kaw393939/is218_test1_official`, copying only `main`. Clone your fork with SSH.
Create and use a local `.venv`, install the supplied requirements, implement the two
functions below, and write the six named tests yourself. Deliver everything on your
fork's `main` with a successful Assessment Tests run for that exact commit.

## Behavior

In `calculator/__init__.py`, define `add(a, b)` and `subtract(a, b)`.
Addition returns the sum of its arguments. Subtraction returns the first argument
minus the second. Both calculate using the supplied arguments and return the result;
printing or returning a fixed answer does not satisfy the specification.

Use integer inputs. Multiplication, division, user input, a command-line interface,
classes, type validation, exception handling, and design patterns are outside scope.

## Student tests

Write these ordinary pytest functions; no parameterization is required. Every test
must call the specified calculator function and assert its returned value equals the
expected result. Keep the exact names so the supplied grader can identify your work.

| File | Test function | Input arguments | Expected return |
| --- | --- | --- | --- |
| `tests/operations/test_add.py` | `test_add` | `2, 3` | `5` |
| `tests/operations/test_add.py` | `test_add_zero` | `7, 0` | `7` |
| `tests/operations/test_add.py` | `test_add_negative` | `-4, 1` | `-3` |
| `tests/operations/test_subtract.py` | `test_subtract` | `5, 3` | `2` |
| `tests/operations/test_subtract.py` | `test_subtract_negative_result` | `3, 5` | `-2` |
| `tests/operations/test_subtract.py` | `test_subtract_zero` | `7, 0` | `7` |

Skipped, expected-failure, missing, or renamed required tests do not count. Extra
tests are welcome but cannot replace these six. The supplied `checks/` tests verify
the same published behaviors independently and cannot replace your own tests.

## Files students create

```text
is218_test1_official/
├── PROJECT.md
├── requirements.txt            # copy provided/requirements.txt
├── pytest.ini                  # copy provided/pytest.ini
├── calculator/
│   └── __init__.py
└── tests/
    └── operations/
        ├── test_add.py
        └── test_subtract.py
```

Preserve the other supplied files, especially `.gitignore`, `.github/`, `checks/`,
`scripts/`, and `provided/`. Do not weaken the grader, skip checks, or change the
workflow condition. Workflows and grading scripts are supplied infrastructure.

## Process and evidence

- Create four issues in **your fork** using the four task files, one at a time.
- Use a separate branch for each issue and include its actual issue number in a
  meaningful commit message. Merge each branch into your fork's `main`.
- Review `git diff` and `git diff --cached`; ensure generated files stay untracked.
- Observe at least one failed assertion while developing a test, then fix the
  implementation. No screenshot, failing commit, or failure report is required.
- In `PROJECT.md`, record your name, project purpose, setup/test instructions,
  links to your four issues, and a brief explanation of what one assertion verifies.
- Close each issue after merging its work. Submission is on `main`.

## Rubric: 100 points

| Area | Points | Evidence |
| --- | ---: | --- |
| Environment and reproducibility | 25 | Local `.venv` (instructor spot-check), installed dependencies, correct configuration, working ignore rules, usable PROJECT instructions. |
| Correct Python behavior | 25 | Both functions calculate from arguments and return correct results. |
| Meaningful student tests | 25 | Six required cases run and pass; assertions actually check calculator results. |
| Git workflow | 15 | Four issues, task branches, issue-referencing commits, and merges into the student's `main`. |
| Final verification and submission | 10 | Successful Assessment Tests run for final `main`, repository URL and matching run URL. |

A green run is required for full credit, but it is not the entire grade. The
instructor reviews assertions, process, and local environment use. GitHub's runner
cannot prove you used `.venv` on your computer. Automated checks are feedback, not
a substitute for instructor review. This rubric does not impose an automatic zero
on an otherwise partial submission with failing CI.
