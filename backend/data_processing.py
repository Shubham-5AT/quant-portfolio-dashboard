import numpy as np
import pandas as pd
df = pd.read_csv("../data/data.csv")
df.columns = df.columns.str.strip()          # remove spaces
df.columns = df.columns.str.replace(" ", "_")  #replace spaces with underscore
#eg - Life Expectancy - Life_Expectancy
df.columns = df.columns.str.replace("(", "")
df.columns = df.columns.str.replace(")", "")
#eg - GDP(USD) - GDP_USD
df = df.drop_duplicates()                    # remove duplicate rows
df = df.fillna(df.mean(numeric_only=True))   # fill numeric missing values
df["Year"] = df["Year"].astype(int) # Ensure Year column is integer.
numeric_cols = df.select_dtypes(include=["float64","int64"]).columns # find all numeric columns
df.to_csv("../data/cleaned_data.csv", index=False) #exports
print("Dataset cleaned successfully")