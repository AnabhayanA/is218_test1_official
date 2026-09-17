# Student Walkthrough

[Home](../README.md) · [Specification](../SPEC.md) · [Troubleshooting](TROUBLESHOOTING.md)

Read one step, do it, and check its expected result before continuing. Run commands
one at a time. Commands go in the terminal; Python and Markdown go in the named
editor files. Save edited files before running checks. Replace example usernames,
issue numbers, and branch names with your own values.

## 0. Before assessment day

**Where:** Your terminal and browser.

**Do:** Check `git --version`, sign in to GitHub, and check Python with
`python3 --version` (macOS/Linux) or `py --version` (Windows PowerShell).
Use Python 3.13 to match the runner. Ask for setup help before the timed assessment
if it is missing. Run:

```bash
ssh -T git@github.com
```

**Expect:** GitHub greets your username and says authentication succeeded but shell
access is unavailable. That message is success even though this command can exit
with status 1. GitHub CLI login and Git SSH authentication are separate; verify SSH.

**If different:** Follow your course's SSH setup instructions or GitHub's
[SSH guide](https://docs.github.com/en/authentication/connecting-to-github-with-ssh).
If this is your first SSH connection, verify the displayed host fingerprint using
GitHub's documentation before accepting it. Never share or commit a private key.

## 1. Fork and clone with SSH

**Where:** GitHub in your browser.

**Do:**

1. Open [the official repository](https://github.com/kaw393939/is218_test1_official).
2. Click **Fork**. Choose your personal account as owner. Keep the repository name
   `is218_test1_official` so the commands below match.
3. Select **Copy the `main` branch only**, then **Create fork**. The completed demo
   is for instructor demonstration; it is not your submission starting point.
4. Confirm the page is `YOUR-USERNAME/is218_test1_official` and says it was forked
   from `kaw393939/is218_test1_official`.
5. Open **Actions** in **your fork**. If prompted, choose **I understand my workflows,
   go ahead and enable them** (wording may vary). If workflows are disabled, enable
   them. Forking alone is not evidence that a workflow ran.
6. On your fork's **Code** tab, choose **Code → SSH** and copy the SSH clone URL.
7. Open **Issues**. If it is missing, use your fork's **Settings → General → Features**
   to enable **Issues**. You will create the four task issues in your fork.

**Where:** Terminal in your coursework directory, outside any other repository.

**Do:** Replace `YOUR-USERNAME`, then run:

```bash
git clone git@github.com:YOUR-USERNAME/is218_test1_official.git
cd is218_test1_official
git remote -v
git branch --show-current
code .
```

If `code .` is unavailable, use your editor's **Open Folder** command.

**Expect:** The branch is `main`. Both `origin` lines use
`git@github.com:YOUR-USERNAME/is218_test1_official.git`. This is your fork, not the
instructor's repository. Cloning already initializes Git; do not run `git init`.

**If different:** Stop and fix the remote before pushing. See
[remote troubleshooting](TROUBLESHOOTING.md). GitHub's
[fork documentation](https://docs.github.com/en/pull-requests/how-tos/work-with-forks/fork-a-repo)
explains the difference between the online fork and your local clone.

## 2. Prove you can push

**Where:** Editor, a new file named `PROJECT.md` at the repository root.

**Do:** Write a project title, your name, and one sentence describing your assignment.
Save, then run:

```bash
git status
git add PROJECT.md
git diff --cached
git commit -m "Identify my assessment project"
git push origin main
```

**Expect:** `PROJECT.md` appears in your fork on GitHub. **Materials Check** passes.
**Assessment Tests** runs and fails because you have not created the project yet.
Open its `assessment` job and read the missing-file messages. This early failure is
expected; it tells you the grader is enabled in your fork.

**If different:** If no run appears, enable workflows in your fork and use
**Actions → Assessment Tests → Run workflow → main**, or make your next commit and
push. If the assessment job is skipped in your fork, check that you are viewing
your repository rather than the instructor's. Do not change the workflow condition.

## 3. Complete Issue 1: setup

**Where:** Your fork's Issues tab, then the terminal and editor.

**Do:** Open [Task 1](../tasks/01-setup.md). Create an issue with its title and copy
its objective and acceptance checklist into the issue body. Note the actual number
GitHub assigns; it may not be `1`. Create the branch:

```bash
git switch main
git pull --ff-only origin main
git switch -c setup
```

Follow the task's setup instructions. Then use this complete review/merge sequence.
Replace `#1` in the messages with your actual setup issue number.

```bash
git status
git diff
git add requirements.txt pytest.ini PROJECT.md
git diff --cached
git commit -m "Set up Python project #1"
git push -u origin setup
git switch main
git pull --ff-only origin main
git merge --no-ff setup -m "Merge Python setup #1"
git push origin main
```

**Expect:** The setup files appear on your fork's `main`. The assessment run still
fails because implementation and tests are missing. Close your setup issue manually
after checking the merged files. A commit containing `#1` references an issue but
does not necessarily close it.

**If different:** Read the actual error before continuing. `git diff` omits untracked
file contents, so also review the staged changes using `git diff --cached`.

## 4. Repeat for addition, subtraction, and delivery

**Do:** Complete [Task 2](../tasks/02-addition.md),
[Task 3](../tasks/03-subtraction.md), and [Task 4](../tasks/04-delivery.md) in order.
Create each issue just before beginning it. Use branches `addition`, `subtraction`,
and `delivery`. Start each from your updated `main`, following the same loop above.

| Task | Stage these files | Example commit message (use your actual issue number) |
| --- | --- | --- |
| Addition | `calculator/__init__.py tests/operations/test_add.py` | `Implement and test addition #2` |
| Subtraction | `calculator/__init__.py tests/operations/test_subtract.py` | `Implement and test subtraction #3` |
| Delivery | `PROJECT.md` | `Document and verify delivery #4` |

Run the local test command in each task before committing. Push each task branch,
merge it into your fork's `main` with `--no-ff`, push `main`, and close the issue.
Use the matching branch name in each Git command. `--no-ff` records a merge even
when Git could simply advance the branch pointer, making your work easy to review.

**Expect:** Addition's local tests pass while the full assessment remains incomplete.
After subtraction, all six student tests and six acceptance cases pass. Delivery
adds the final documentation and issue links. Earlier red runs remain in history;
there is no need to delete them.

**If different:** If you choose to use a pull request instead of the documented local
merge, set the **base repository to YOUR fork** and the base branch to `main`. GitHub
may otherwise suggest the instructor's repository. A pull request is optional.

## 5. Verify and submit

Follow the [submission checklist](SUBMISSION.md). In your fork, choose the
**Assessment Tests** push run for the final `main` commit. Confirm the `assessment`
job and its last verification step actually executed and passed. A skipped job,
queued run, older successful run, or green Materials Check alone is insufficient.

Submit your repository URL and that run's URL in the instructor's submission system.
Any later changes need a new successful run.
