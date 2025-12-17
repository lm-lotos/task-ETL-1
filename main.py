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
