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

# 4. Feature engineering

# full name
df_clean["full_name"] = df_clean["first_name"] + " " + df_clean["last_name"]

# email domain
df_clean["email_domain"] = df_clean["email"].str.split("@").str[-1]

# city name length
df_clean["city_length"] = df_clean["city"].str.len()

# gmail flag
df_clean["is_gmail"] = df_clean["email_domain"] == "gmail.com"

print("\n=== FEATURE ENGINEERING PREVIEW ===")
print(df_clean[["full_name", "email_domain", "city_length", "is_gmail"]].head())

# 5. Data filtering and segmentation

# users with gmail.com
gmail_users = df_clean.loc[df_clean["is_gmail"]]

# companies with LLC or Ltd in name
llc_ltd_companies = df_clean.loc[
    df_clean["company_name"].str.contains("LLC|Ltd", case=False, na=False)
]

# people from London
london_users = df_clean.loc[df_clean["city"] == "London"]

# companies with name length >= 4 words
df_clean["company_word_count"] = df_clean["company_name"].str.split().str.len()
long_company_names = df_clean.loc[df_clean["company_word_count"] >= 4]

# positional selections
first_10_rows = df_clean.iloc[:10, 2:6]
every_10th_row = df_clean.iloc[::10]
random_5_rows = df_clean.sample(5)

print("\n=== FILTERING RESULTS ===")
print("Gmail users:", len(gmail_users))
print("LLC/Ltd companies:", len(llc_ltd_companies))
print("London users:", len(london_users))
print("Long company names:", len(long_company_names))

