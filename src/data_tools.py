import pandas as pd
from pathlib import Path


DATA_FOLDER = Path("data")


FILES = {
    "students": "students.csv",
    "courses": "courses.csv",
    "assessments": "assessments.csv",
    "attendance": "attendance.csv",
    "mentors": "mentors.csv"
}


def load_table(table_name):

    if table_name not in FILES:
        raise ValueError("Unknown dataset")

    path = DATA_FOLDER / FILES[table_name]

    if not path.exists():
        raise FileNotFoundError(path)

    if path.stat().st_size == 0:
        raise ValueError(f"{path.name} is empty")

    return pd.read_csv(path)


def find_records(table_name, search_value):

    df = load_table(table_name)

    search_value = str(search_value).strip().lower()

    matches = pd.Series(False, index=df.index)

    for column in df.columns:

        column_values = df[column].astype(str).str.lower()

        matches |= column_values.eq(search_value)

    result = df[matches]

    return result.head(20).to_dict(orient="records")


def search_student(student_id: str):

    return find_records("students", student_id)


def search_course(course_id: str):

    return find_records("courses", course_id)


def search_assessment(student_id: str):

    return find_records("assessments", student_id)


def search_attendance(student_id: str):

    return find_records("attendance", student_id)


def search_mentor(mentor_id: str):

    return find_records("mentors", mentor_id)