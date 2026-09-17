# IS 218 Test 1: Build, Test, and Deliver

You are joining a development team. Your first assignment is to deliver a small
Python calculator package that another developer can download, install, and test.
You will implement addition and subtraction and prove they work locally and on GitHub.

**Start by forking this repository into your own GitHub account. Copy only `main`,
then clone your fork using SSH.** Follow the [student walkthrough](docs/WALKTHROUGH.md)
from the beginning. Do not create an unrelated empty repository for this test.

## Rules and resources

- Write the Python functions and student tests yourself. Do not use AI to generate,
  complete, rewrite, or repair your implementation or tests. Disable AI inline code
  completion for these files during the assessment.
- You may use this handout, the supplied setup files, the
  [preparation manual](https://github.com/kaw393939/is218_sample_test), class recordings,
  and setup/command references. Read explanations; write your own solution. Do not
  copy completed implementation or test files from the sample or demo.
- The supplied workflow, grading scripts, and acceptance checks stay unchanged.
- Work in your own fork. Push and merge into **your fork's `main`**.
- The instructor announces the actual time limit, deadline, and submission location.
  The planned working time is 60–75 minutes after the tool/access preflight.

## Your path

| Stage | Work | Complete when |
| --- | --- | --- |
| Start | [Fork, enable Actions, and clone over SSH](docs/WALKTHROUGH.md#1-fork-and-clone-with-ssh) | `origin` points to your fork using `git@github.com:`. |
| Issue 1 | [Set up Python and pytest](tasks/01-setup.md) | Your project environment runs pytest. |
| Issue 2 | [Write addition and three tests](tasks/02-addition.md) | All three addition tests pass. |
| Issue 3 | [Write subtraction and three tests](tasks/03-subtraction.md) | All six student tests pass. |
| Issue 4 | [Document and deliver](tasks/04-delivery.md) | Your final `main` commit passes **Assessment Tests**. |

For each issue: **issue → branch → write → test → review → commit → push → merge → verify**.
The [walkthrough](docs/WALKTHROUGH.md) supplies the Git and setup commands, not your Python solution.

## Submit

Submit your fork's repository URL and the successful **Assessment Tests** run URL
for its final `main` commit. A green **Materials Check** alone is not a passing test.
See the [specification and rubric](SPEC.md) and [submission checklist](docs/SUBMISSION.md).

## What is supplied?

The starter includes instructions, `.gitignore`, workflows, grading tools, public
acceptance checks, and configuration files in `provided/`. You copy the two setup
files to the project root and create `calculator/`, `tests/`, and `PROJECT.md` yourself.
The `.venv` directory stays on your computer and is never committed.

## Instructor branches and checks

- **`main`** is the unfinished student starter. **Materials Check** verifies the
  distribution. On the official repository's `main` only, the assessment job is
  intentionally skipped; this is not a completed submission.
- **`demo-complete`** is the
  [instructor's completed demonstration](https://github.com/kaw393939/is218_test1_official/tree/demo-complete).
  Its **Assessment Tests** job must run and pass. Use it for the instructor-led
  walkthrough or review after submission, not as the source of your answer.
- **Your fork:** Assessment Tests runs on every push, pull request, and manual run,
  including `main`. Early failures for missing work are expected. Finish the tasks
  and get a successful run with an executed `assessment` job.

[Troubleshooting](docs/TROUBLESHOOTING.md) · [Instructor notes](instructor/README.md)
