# Demonstration of Continuous Integration Using Travis CI

[![Build Status](https://app.travis-ci.com/<YOUR_GITHUB_USERNAME>/ci-travis-demo.svg?branch=main)](https://app.travis-ci.com/<YOUR_GITHUB_USERNAME>/ci-travis-demo)
[![Python Version](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue.svg)](https://www.python.org/)
[![Testing Framework](https://img.shields.io/badge/tested%20with-pytest-yellow.svg)](https://docs.pytest.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

A complete, beginner-friendly DevOps college practical project demonstrating **Continuous Integration (CI)** with **Travis CI**, **GitHub**, and **Python (pytest)**.

---

## Table of Contents

1. [Project Overview & Objectives](#project-overview--objectives)
2. [What is Continuous Integration (CI)?](#what-is-continuous-integration-ci)
3. [What is Travis CI?](#what-is-travis-ci)
4. [Technology Stack](#technology-stack)
5. [Project Directory Structure](#project-directory-structure)
6. [Local Installation and Setup](#local-installation-and-setup)
7. [Running the Application and Test Suite](#running-the-application-and-test-suite)
8. [Understanding the `.travis.yml` Configuration](#understanding-the-travisyml-configuration)
9. [Step-by-Step GitHub and Travis CI Integration](#step-by-step-github-and-travis-ci-integration)
10. [How Automatic Builds Work](#how-automatic-builds-work)
11. [Expected Build Results (Pass vs. Fail)](#expected-build-results-pass-vs-fail)
12. [Demonstration Guide for College Viva / Practical](#demonstration-guide-for-college-viva--practical)
13. [Troubleshooting Guide](#troubleshooting-guide)

---

## Project Overview & Objectives

In modern software engineering, manual testing and integration create bottlenecks and allow regression bugs to enter production. The objective of this project is to build and demonstrate a working Continuous Integration (CI) pipeline that:
- Automatically listens for new code commits pushed to a remote GitHub repository.
- Spins up an isolated virtual Linux build environment on **Travis CI**.
- Automatically installs required dependencies (`pytest`).
- Executes 18 automated unit and edge-case tests across multiple Python versions (3.10, 3.11, 3.12).
- Signals immediate feedback: green badge / build success when all tests pass, or red alert / build failure if an error or bug is introduced.

---

## What is Continuous Integration (CI)?

**Continuous Integration (CI)** is a fundamental DevOps software development practice where team members integrate their code alterations into a shared central repository frequently (usually multiple times a day). 

Each integration is automatically verified by:
1. **Automated Builds**: Compiling or packaging code to check integrity.
2. **Automated Testing**: Running unit, regression, and integration tests against the new changes.

### Key Benefits of CI
- **Early Bug Detection**: Defects are identified minutes after being introduced rather than weeks later during release staging.
- **Elimination of Integration Hell**: Merging small changes continuously avoids conflicting codebases.
- **Immediate Developer Feedback**: Developers know within minutes if their latest push broke existing functionality.
- **Consistent Testing Environment**: Tests run in clean, reproducible virtual containers rather than suffering from "it works on my machine" discrepancies.

---

## What is Travis CI?

**Travis CI** is a hosted continuous integration service used to build and test software projects hosted on GitHub and Bitbucket. 

When code is pushed to GitHub, Travis CI:
- Receives a webhook notification from GitHub.
- Provisions a clean virtual container (Ubuntu Jammy).
- Reads `.travis.yml` located in the root of the repository.
- Executes build and test lifecycle commands.
- Reports build status back to GitHub via commit status badges and check markers.

---

## Technology Stack

| Technology | Purpose | Version |
| :--- | :--- | :--- |
| **Python** | Application programming language | 3.10+ / 3.11 / 3.12 |
| **pytest** | Automated test runner and assertion framework | >= 8.0.0 |
| **Git** | Distributed Version Control System | 2.x+ |
| **GitHub** | Remote Git code hosting and webhook provider | Cloud |
| **Travis CI** | Continuous Integration build runner | Cloud (app.travis-ci.com) |
| **Markdown** | Project and academic documentation | Standard GFM |

---

## Project Directory Structure

```text
ci-travis-demo/
├── .gitignore                  # Files and patterns ignored by Git
├── .travis.yml                 # Travis CI build, environment, and test configuration
├── calculator.py               # Core application logic (arithmetic functions)
├── test_calculator.py          # Pytest automated test suite (18 test cases)
├── requirements.txt            # Python dependencies (pytest)
├── README.md                   # Project overview, installation, and usage guide
└── docs/
    └── project_documentation.md # Detailed academic college project report
```

---

## Local Installation and Setup

### 1. Prerequisites
Ensure you have the following installed on your machine:
- **Python 3.10 or higher**: [python.org](https://www.python.org/downloads/)
- **Git**: [git-scm.com](https://git-scm.com/)

### 2. Clone the Repository (or navigate to workspace)
```bash
git clone https://github.com/<YOUR_GITHUB_USERNAME>/ci-travis-demo.git
cd ci-travis-demo
```

### 3. (Optional but Recommended) Create a Virtual Environment
- **On Windows (PowerShell):**
  ```powershell
  python -m venv venv
  .\venv\Scripts\Activate.ps1
  ```
- **On Linux / macOS:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 4. Install Dependencies
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

---

## Running the Application and Test Suite

### Running the Calculator Directly
Execute `calculator.py` to see sample output:
```bash
python calculator.py
```
**Output:**
```text
==================================================
 Python Calculator - CI Demonstration Module
==================================================
Addition:       10 + 5    = 15
Subtraction:    10 - 5    = 5
Multiplication: 10 * 5    = 50
Division:       10 / 5    = 2.0
==================================================
Module executed successfully. Run pytest to execute test suite.
```

### Running the Automated Tests Locally
Run pytest with verbose output:
```bash
pytest -v
```
or via the Python module:
```bash
python -m pytest -v
```

**Expected Local Output:**
```text
============================= test session starts =============================
platform win32 -- Python 3.14.2, pytest-9.1.1, pluggy-1.6.0
rootdir: C:\Users\surya\Downloads\devops project
collected 18 items

test_calculator.py::test_add_positive_integers PASSED                    [  5%]
test_calculator.py::test_add_negative_integers PASSED                    [ 11%]
test_calculator.py::test_add_mixed_sign_integers PASSED                  [ 16%]
test_calculator.py::test_add_with_zero PASSED                            [ 22%]
test_calculator.py::test_add_floating_point_numbers PASSED               [ 27%]
test_calculator.py::test_subtract_positive_integers PASSED               [ 33%]
test_calculator.py::test_subtract_negative_integers PASSED               [ 38%]
test_calculator.py::test_subtract_with_zero PASSED                       [ 44%]
test_calculator.py::test_subtract_floating_point_numbers PASSED          [ 50%]
test_calculator.py::test_multiply_positive_integers PASSED               [ 55%]
test_calculator.py::test_multiply_negative_integers PASSED               [ 61%]
test_calculator.py::test_multiply_with_zero PASSED                       [ 66%]
test_calculator.py::test_multiply_floating_point_numbers PASSED          [ 72%]
test_calculator.py::test_divide_positive_numbers PASSED                  [ 77%]
test_calculator.py::test_divide_negative_numbers PASSED                  [ 83%]
test_calculator.py::test_divide_floating_point_numbers PASSED            [ 88%]
test_calculator.py::test_divide_by_zero_raises_exception PASSED          [ 94%]
test_calculator.py::test_invalid_input_types_raise_type_error PASSED     [100%]

============================= 18 passed in 0.12s ==============================
```

---

## Understanding the `.travis.yml` Configuration

The `.travis.yml` configuration file instructs Travis CI on how to set up the environment and test the code:

```yaml
# 1. Declare the runtime language
language: python

# 2. Specify OS and Ubuntu distribution
os: linux
dist: jammy

# 3. Define the build matrix (Python versions to test against)
python:
  - "3.10"
  - "3.11"
  - "3.12"

# 4. Commands executed before running tests
install:
  - python -m pip install --upgrade pip
  - pip install -r requirements.txt

# 5. The core CI step - execute test suite
# Any non-zero exit code here immediately triggers build failure
script:
  - pytest -v --tb=short

# 6. Build notifications
notifications:
  email: false
```

### Breakdown of Key Directives:
- `language: python`: Tells Travis CI to provision an image with Python tooling.
- `dist: jammy`: Uses Ubuntu 22.04 LTS (Jammy Jellyfish), ensuring modern C-libraries and Python versions.
- `python: [...]`: Matrix build. Travis will spin up **3 concurrent jobs**, running tests across Python 3.10, 3.11, and 3.12.
- `install`: Upgrades package installer and installs dependencies from `requirements.txt`.
- `script`: The decisive test command. If `pytest` exits with code `0`, the build succeeds. If any test fails, `pytest` returns exit code `1`, causing Travis CI to mark the entire build as failed.

---

## Step-by-Step GitHub and Travis CI Integration

Follow these steps to link this project with Travis CI:

### Step 1: Initialize Git and Push to GitHub
1. Open your terminal in the project directory.
2. If not already initialized, run:
   ```bash
   git init -b main
   git add .
   git commit -m "Initial commit: Calculator application with pytest suite and Travis CI config"
   ```
3. Create a new public repository on [GitHub](https://github.com/new) named `ci-travis-demo`.
4. Link and push your local repository:
   ```bash
   git remote add origin https://github.com/<YOUR_GITHUB_USERNAME>/ci-travis-demo.git
   git push -u origin main
   ```

### Step 2: Connect GitHub with Travis CI
1. Navigate to **[https://app.travis-ci.com](https://app.travis-ci.com)**.
2. Click **"Sign in with GitHub"**.
3. Authorize Travis CI to access your GitHub account.
4. On the Travis CI dashboard, click your profile icon (top right) or navigate to **Accounts / Repositories**.
5. Click **"Activate"** or **"Manage repositories on GitHub"**.
6. Select the `ci-travis-demo` repository and click **Approve & Install**.
7. Flip the toggle switch to **ON** for `ci-travis-demo`.

### Step 3: Trigger the First Build
- Once activated, pushing any commit to `main` automatically queues a build.
- You can trigger your first build manually on Travis CI by clicking **"Trigger build"** or by making a small commit:
  ```bash
  git commit --allow-empty -m "Trigger initial Travis CI build"
  git push origin main
  ```

---

## How Automatic Builds Work

```
+------------------+         git push          +--------------------+
| Local Developer  |  --------------------->  | GitHub Repository  |
| Machine          |                          +--------------------+
+------------------+                                     |
                                                         | Webhook Event
                                                         v
                                              +--------------------+
                                              |     Travis CI      |
                                              +--------------------+
                                                         |
                            +----------------------------+----------------------------+
                            |                            |                            |
                            v                            v                            v
                     [Job 1: Py 3.10]             [Job 2: Py 3.11]             [Job 3: Py 3.12]
                            |                            |                            |
                            v                            v                            v
                     - pip install                - pip install                - pip install
                     - pytest -v                  - pytest -v                  - pytest -v
                            |                            |                            |
                            +----------------------------+----------------------------+
                                                         |
                                                         v
                                              +--------------------+
                                              | Build Status (✓/✗) |
                                              +--------------------+
```

1. **Commit & Push**: A developer makes changes and runs `git push`.
2. **GitHub Webhook**: GitHub sends a payload to Travis CI containing commit information.
3. **Container Provisioning**: Travis CI launches isolated virtual machines according to the matrix specified in `.travis.yml`.
4. **Execution**: The script executes `pip install -r requirements.txt` followed by `pytest -v`.
5. **Feedback Loop**: Results are posted to Travis CI logs and GitHub commits/pull requests.

---

## Expected Build Results (Pass vs. Fail)

### Successful Build Log Example (Travis CI)
```text
$ pytest -v --tb=short
============================= test session starts =============================
collecting ... collected 18 items
test_calculator.py::test_add_positive_integers PASSED                    [  5%]
...
test_calculator.py::test_divide_by_zero_raises_exception PASSED          [ 94%]
test_calculator.py::test_invalid_input_types_raise_type_error PASSED     [100%]
============================= 18 passed in 0.12s ==============================
The command "pytest -v --tb=short" exited with 0.
Done. Your build exited with 0. (PASSED)
```

### Failed Build Log Example (Travis CI)
```text
$ pytest -v --tb=short
============================= test session starts =============================
collecting ... collected 18 items
test_calculator.py::test_add_positive_integers FAILED                    [  5%]

=================================== FAILURES ===================================
__________________________ test_add_positive_integers __________________________
test_calculator.py:17: in test_add_positive_integers
    assert add(5, 7) == 12
E   assert 13 == 12
=========================== short test summary info ============================
FAILED test_calculator.py::test_add_positive_integers - assert 13 == 12
========================= 1 failed, 17 passed in 0.14s =========================
The command "pytest -v --tb=short" exited with 1.
Done. Your build exited with 1. (FAILED)
```

---

## Demonstration Guide for College Viva / Practical

Use this 3-step demonstration to clearly show your evaluator how Continuous Integration protects the codebase:

### Stage 1: Demonstrate a Passing Build
1. Ensure `calculator.py` is working properly.
2. Push changes:
   ```bash
   git push origin main
   ```
3. Show the Travis CI dashboard:
   - Status changes to **Passed** (Green).
   - Show all 18 test cases passing across Python versions.

### Stage 2: Introduce an Intentional Bug (Demonstrate Failure)
1. Open `calculator.py` and modify the `add` function:
   ```python
   def add(a, b):
       return a + b + 1  # BUG: Returns incorrect sum
   ```
2. Commit and push the bug:
   ```bash
   git add calculator.py
   git commit -m "Introduce bug in add function for CI failure demonstration"
   git push origin main
   ```
3. Switch to Travis CI:
   - Notice the build starts automatically.
   - Watch the build turn **Failed / Errored** (Red).
   - Point out the failure traceback highlighting `assert 13 == 12`.
   - Explain to the examiner: *“The CI server caught the bug immediately before code could ever reach deployment.”*

### Stage 3: Fix the Bug and Restore Passing Status
1. Revert `calculator.py` back to:
   ```python
   def add(a, b):
       return a + b
   ```
2. Commit and push the fix:
   ```bash
   git add calculator.py
   git commit -m "Fix bug in add function: restore clean CI build"
   git push origin main
   ```
3. Refresh Travis CI:
   - A new build triggers automatically.
   - Status returns to **Passed** (Green).

---

## Troubleshooting Guide

| Issue | Cause | Solution |
| :--- | :--- | :--- |
| **Travis CI doesn't trigger on push** | Repository is not active in Travis CI settings or webhook is missing | Visit `app.travis-ci.com/profile`, sync account, and verify repository toggle is ON. |
| **`pytest: command not found` on Travis** | `requirements.txt` was not installed | Verify `install` block in `.travis.yml` contains `pip install -r requirements.txt`. |
| **Local `pytest` not recognized** | `pytest` is not in PATH or not installed in current environment | Run via `python -m pytest` or activate your virtual environment. |
| **Git push rejected (non-fast-forward)** | Remote repo has commits (e.g. default README created on GitHub) | Run `git pull --rebase origin main` then `git push origin main`. |
| **Travis CI Free Tier Credits** | Travis CI open-source accounts receive trial credits | For educational accounts, request education tier credits on Travis CI or demonstrate using the CLI/build log viewer. |

---

## Academic Information
- **Course**: DevOps / Software Engineering Practical
- **Topic**: Continuous Integration Workflow using Travis CI
- **Author**: Student Demonstration Project
- **Documentation**: Refer to [docs/project_documentation.md](docs/project_documentation.md) for the complete academic report.
