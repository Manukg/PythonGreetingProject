# Python Greeting Project

[![Python application](https://github.com/Manukg/PythonGreetingProject/actions/workflows/main.yml/badge.svg)](https://github.com/Manukg/PythonGreetingProject/actions/workflows/main.yml)

This repository uses **GitHub Actions** for CI:

- Linting with `pylint`
- Unit testing with `unittest`
- Automatic builds on `push` and `pull request` to `main`

---

## Triggering the Workflow

### Automatic Triggers
The workflow runs automatically on:

- **Push** to the `main` branch
- **Pull request** targeting the `main` branch

### Manual Trigger (`workflow_dispatch`)
You can manually run the workflow:

1. Go to **GitHub → Actions → Python application workflow**.
2. Click **“Run workflow”**.
3. Optionally, provide input parameters if defined.
4. Click **Run workflow**.

**Notes:**

- Manual runs create a **new workflow run** using the latest code.
- Runs are executed on a **fresh GitHub-hosted virtual machine**.
- Nothing changes in your local repository.

### Re-run Existing Workflow
If a workflow run fails, click **“Re-run all jobs”** on that run’s page to retry the same workflow:

- Uses the **same commit/code** as the original run.
- Useful for debugging intermittent issues.

---
 

### Set up all required parameters in the Secrets section in GitHub.

- Modified the workflow .yml file to send an email when linting or testing fails, using the dawidd6 action-send-mail@v3 action.