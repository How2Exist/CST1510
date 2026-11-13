"""
RECORD CHECK  -  my version
===========================

Name  :  Stefan Valev
Lane  :  IT
Date  :  7/11/2026

Run it:   python/python3 CSVDataframe.py
"""

# Importing necessities
import pandas as pd
import os
import matplotlib.pyplot as plt

# Create the dataframe from an existing .csv file
df = pd.DataFrame(pd.read_csv("/Users/stefan/Programming_stuff/Github_stuff/CST1510/Week 06 - Pandas/LAB/records_sample.csv"))

# Creating a new column "percent" with the percent of rows usedGB and totalGB
df["percent"] = (df["usedGB"] / df["totalGB"]) * 100
# Creating a new column "status" by checking percent from the column "percent"
df["status"] = df["percent"].apply(lambda p: "OVER LIMIT" if p >= 100 else ("WARNING" if p >= 90 and p < 100 else "OK"))


# Threshold (print dataframe):
print (df)

# Typical (print dataframe without rows that have "OK" status):
print (df[df["status"] != "OK"])

# Excellent (print dataframe with grouping, create and save to new .csv file, display grouping as a bar chart):

# Print dataframe with grouping and filter by "status"
print(df.groupby("status").size())

# Create new .csv file and save dataframe to it
df.to_csv("Datafram.csv", index=False)

# Display values in column "status" in a bar chart
# Have to manually create "counts", I remember it existing before...
counts = df["status"].value_counts()
counts.plot(kind="bar", rot=0)
plt.show()