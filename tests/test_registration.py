from src.student_registration import register_student


def test_valid_registration():
    assert register_student(
        "Ada",
        "ada@example.com",
        "ada@university.edu"
    ) == "Student registered successfully"


def test_missing_name():
    assert register_student(
        "",
        "ada@example.com",
        "ada@university.edu"
    ) == "Invalid student details"


def test_missing_email():
    assert register_student(
        "Ada",
        "",
        "ada@university.edu"
    ) == "Invalid student details"


def test_missing_institutional_email():
    assert register_student(
        "Ada",
        "ada@example.com",
        ""
    ) == "Invalid student details"
