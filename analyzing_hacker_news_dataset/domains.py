import read
import pandas as pd 
df = read.load_data("hn_stories.csv")
domain = df["url"].value_counts().sort_values(ascending = False)
print(domain.iloc[0:10])






