import pandas as pd
from pathlib import Path

for path in Path("data").glob("*.csv"):

    df = pd.read_csv(path)

    print("\nFILE:", path.name)

    print("Columns:", list(df.columns))

    print("Data types:")
    print(df.dtypes)

    print("Missing values:")
    print(df.isnull().sum())