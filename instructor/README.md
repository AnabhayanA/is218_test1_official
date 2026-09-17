# Instructor Notes

## Teaching scope

This is a first guided assessment connecting the IS 117 issue/branch/review/merge
loop with Python environments, simple functions, pytest, and CI. Students write
the implementation and student tests themselves; setup references are allowed.
The current test is **fork-based**, superseding the sample manual's instruction to
create an unrelated empty repository. Follow this official handout for submission.

There are four task issues. No generated Python solutions, AI inline completions,
classes, multiplication/division, or design patterns are required. A failing
assertion is a learning checkpoint, not a screenshot or commit requirement.

## Before class

- Announce the deadline, time limit, and submission location. Plan for 60–75 minutes
  plus a separate preflight for Python 3.13, SSH, and GitHub access.
- Keep `main` the default branch. Students fork **only main** and clone using SSH.
- Check Materials Check on instructor `main` and Assessment Tests on `demo-complete`.
- Explain that forks may need Actions and Issues enabled explicitly.
- Demonstrate the distinction between origin (student fork) and the instructor repo.
- Do not protect student `main` with a requirement that the full assessment be
  green before each early merge: setup and addition are intentionally incomplete.

## Branch design and CI

`main` holds instructions, supplied infrastructure, and setup reference files. It
does not contain `calculator/`, student `tests/`, root requirements/configuration,
or a completed PROJECT. `demo-complete` adds those deliverables in readable commits.
Do not merge the completed demonstration into `main`.

Both branches have the same two workflows:

| Context | Materials Check | Assessment Tests |
| --- | --- | --- |
| Official `main` push/manual run | Executes | Assessment job intentionally skipped |
| Official `demo-complete` push/manual run | Executes | Full assessment executes |
| Student fork, any pushed branch/manual run | Executes | Full assessment executes |
| Pull request | Executes | Full assessment executes |

The sole starter exemption checks both the exact official repository name and
`refs/heads/main`; it never exempts a student's `main`. A skipped job is not a grade.
The six supplied contract cases test the published behaviors; the report verifier
also requires all six named student tests to pass without skips or xfail. Missing
required files fail early with actionable messages and a summary table.

The workflows use read-only repository permissions and require no student secrets.
Students use SSH for their local clone/push operations; Actions uses its built-in
checkout credentials. These are different authentication contexts.

## Demo walkthrough

Switch GitHub's branch selector to `demo-complete` after demonstrating the starter.
Walk through the setup, addition, subtraction, and delivery commits in order.
PROJECT clearly labels the example; demonstration commits are authored by the
instructor and do not pretend to be a student's issue/branch history.

The demo is publicly accessible. “Copy main only” keeps the fork clean but is not
an access control mechanism. Assess independent work using the course rules,
student history, and discussion of their assertions. The demo's successful CI
proves executable behavior, not a completed student's process grade.

## Review and maintenance

Use the rubric in SPEC. Review meaningful assertions and actual calculation, not
just green checks. Spot-check local interpreter selection and inspect the student's
four issue links and merge history. A reference like `#2` alone does not prove that
the issue exists or was completed. No automated process grade is claimed.

Students can edit files in their forks, so workflow results alone are not tamper-proof
grading. Compare `.github/`, `scripts/`, `checks/`, and `provided/` with this repository
when reviewing; investigate altered checks before assigning full credit.

After maintenance, validate the starter and completed demo, including negative
cases: missing/renamed/skipped tests, incorrect arithmetic, and tracked environments.
Keep shared instructions and grading files synchronized across both branches without
bringing the completed solution onto `main`.
