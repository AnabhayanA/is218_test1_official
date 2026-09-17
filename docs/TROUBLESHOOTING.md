# Troubleshooting

[Home](../README.md) · [Walkthrough](WALKTHROUGH.md)

| Symptom | What to check or do |
| --- | --- |
| `Permission denied (publickey)` | Run `ssh -T git@github.com`; confirm the greeting is your account. Check your course SSH setup. GitHub CLI authentication alone does not configure Git SSH. |
| `origin` uses HTTPS or points to the instructor | Run `git remote set-url origin git@github.com:YOUR-USERNAME/is218_test1_official.git` using your account, then check `git remote -v`. |
| Clone destination already exists | Inspect the folder. Use your existing assessment clone if it is correct; do not delete coursework or clone inside it. |
| Issues tab is missing in my fork | Enable Issues in your fork's Settings → General → Features. Create issues in your fork, not the instructor repo. |
| No workflow run appears | Enable Actions in your fork. Verify `.github/workflows/tests.yml` is present. Use Run workflow on `main` or push a new commit. |
| Assessment job is skipped | Official instructor `main` intentionally skips it. In your fork it must execute. Check the repository shown in the URL and preserve the supplied workflow. |
| Only Materials Check is green | Open Assessment Tests separately. Materials Check does not grade your Python. |
| Missing-file errors in early runs | Expected until you create and commit every required project file. Read the file list and continue the tasks. |
| `python` is not found | Activate the environment first. Use `python3` or `py -3.13` when creating it, as documented for your OS. |
| PowerShell blocks activation | Use `.\.venv\Scripts\python.exe` in place of `python`; select that interpreter in the editor. |
| `No module named pytest` | Check `python -c "import sys; print(sys.executable)"`, then install with `python -m pip install -r requirements.txt` in that environment. |
| Cannot import `calculator` | Run from the repository root; check `calculator/__init__.py`, saved files, and the copied `pytest.ini`. |
| `No tests ran` | Check that the saved files and functions start with `test_`, in `tests/operations/`. |
| Test returns `None` | Check that the implementation returns a result rather than only printing it. |
| Required test not passed | Use the exact names from SPEC. Missing, renamed, skipped, or expected-failure required tests do not count. |
| Tests pass locally but files are missing remotely | Check `git status`, stage/review/commit the files, and push the branch. An untracked local file is absent on the runner. |
| Environment/cache files were committed | Run `git rm -r --cached .venv` for an accidentally tracked `.venv` (use the actual offending path for other files). This keeps local files. Preserve ignore rules, commit the removal, and push. |
| Push is rejected because remote has newer work | On the affected branch, run `git pull --ff-only origin BRANCH` with its real name. If it cannot fast-forward, ask for help resolving the difference; do not force-push. |
| A pull request targets the instructor | Change its base repository to your own fork and base branch to `main`, or follow the documented local merge. |

Read the first failed Actions step. Correct the cause locally, run the relevant
tests, commit, and push. Old failed runs remain useful history. Never disable a
check or change an expected answer just to make the dashboard green.
