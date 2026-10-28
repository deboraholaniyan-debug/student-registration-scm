def register_student(name, email, institutional_email):
    if not name or not email or not institutional_email:
        return "Invalid student details"

    return "Student registered successfully"


if __name__ == "__main__":
    print(
        register_student(
            "Ada",
            "ada@example.com",
            "ada@university.edu"
        )
    )

