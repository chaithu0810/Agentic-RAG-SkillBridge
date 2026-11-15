
import pandas as pd

df = pd.read_csv("data/students.csv")

print("COLUMN NAMES:")
print(df.columns.tolist())

print("\nTOTAL STUDENTS:")
print(len(df))

print("\nFIRST 10 RECORDS:")
print(df.head(10).to_string(index=False))

print("\nPOSSIBLE STUDENT ID COLUMNS:")

for col in df.columns:

    if "student" in col.lower() and "id" in col.lower():

        print("\nColumn:", col)

        print("Sample IDs:")
        print(df[col].head(20).tolist())
