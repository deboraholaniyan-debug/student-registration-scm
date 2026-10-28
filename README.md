# student-registration-scm
SEN 401 Software Configuration Management Lab.
# Student Registration System

## Project Overview

The Student Registration System is a small software project
used to demonstrate Software Configuration Management (SCM)
principles with Git and GitHub.

The initial version validates a student's name and personal
email address. A subsequent change introduces institutional
email validation.

## Project Objectives

- Identify and control software configuration items.
- Track changes using Git.
- Manage feature development through branches.
- Review proposed changes through pull requests.
- Maintain a changelog and versioned release.

## Project Structure

- `src/`: Registration application logic.
- `design/`: System design documentation.
- `tests/`: Registration test cases.
- `database/`: Database schema.
- `deployment/`: Execution and deployment instructions.

## Requirements

- Python 3
- Git
- A GitHub account

## Running the Application

From the repository root, run:


python src/student_registration.py


On Windows, you may use:

py src/student_registration.py


## Testing

Install pytest if it is not already available:


python -m pip install pytest


Run the tests from the repository root:


python -m pytest -v

