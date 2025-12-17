# ETL-1 project
# Dataset: UK-500

import pandas as pd
import numpy as np

pd.set_option("display.max_columns", 50)
pd.set_option("display.width", 120)

# 1. Extract & initial exploration
url = "https://s3-eu-west-1.amazonaws.com/shanebucket/downloads/uk-500.csv"
df = pd.read_csv(url)

print("=== HEAD ===")
print(df.head())

print("\n=== INFO ===")
print(df.info())

print("\n=== DESCRIBE ===")
print(df.describe())
# 2. Data quality check: missing values and duplicates

print("\n=== MISSING VALUES ===")
print(df.isna().sum())

print("\n=== DUPLICATES ===")
print("Number of duplicate rows:", df.duplicated().sum())

# 3. Data cleaning

# work on a copy to avoid modifying original dataframe
df_clean = df.copy()

# drop rows that are completely empty
df_clean = df_clean.dropna(how="all")

# remove duplicate rows
df_clean = df_clean.drop_duplicates()

# standardize text columns (strip spaces)
text_cols = df_clean.select_dtypes(include="object").columns
for col in text_cols:
    df_clean[col] = df_clean[col].str.strip()

print("\n=== CLEANED DATA INFO ===")
print(df_clean.info())

