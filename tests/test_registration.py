from src.student_registration import register_student


def test_valid_registration():
    assert register_student(
        "Ada",
        "ada@example.com"
    ) == "Student registered successfully"


def test_missing_name():
    assert register_student(
        "",
        "ada@example.com"
    ) == "Invalid student details"


def test_missing_email():
    assert register_student(
        "Ada",
        ""
    ) == "Invalid student details"
