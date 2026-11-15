import pandas as pd
from pathlib import Path

for filename in [
    "train.csv",
    "test.csv",
    "sample_submission.csv"
]:

    path = Path(filename)

    if path.exists():

        df = pd.read_csv(path)

        print("\nFILE:", filename)

        print("Shape:", df.shape)

        print("Columns:", df.columns.tolist())

        print(df.head())