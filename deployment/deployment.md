# Deployment and Execution Instructions

## Requirements

- Python 3
- Git

## Obtain the Project

Clone the repository from GitHub and enter the project directory.

## Run the Application

From the repository root, run:


python src/student_registration.py


On Windows, use `py` if required.

## Run the Tests

Install pytest if necessary:


python -m pip install pytest


Execute the tests:


python -m pytest -v


## Expected Behaviour

A valid registration should return a success message.
Missing required information should return an error message.

## Limitations

This practical uses a small example. It does not provide
a complete production registration system or live database.
