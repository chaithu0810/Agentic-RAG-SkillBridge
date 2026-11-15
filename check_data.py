import pandas as pd
from pathlib import Path

data_folder = Path("data")

files = [
    "students.csv",
    "courses.csv",
    "assessments.csv",
    "attendance.csv",
    "mentors.csv"
]

for filename in files:

    path = data_folder / filename

    print("\n" + "=" * 50)
    print("FILE:", filename)

    if not path.exists():
        print("ERROR: File not found")
        continue

    if path.stat().st_size == 0:
        print("ERROR: File is empty")
        continue

    try:

        df = pd.read_csv(path)

        print("Rows:", len(df))
        print("Columns:", df.columns.tolist())

        print("\nFirst 3 records:")
        print(df.head(3))

    except Exception as e:

        print("ERROR:", e)