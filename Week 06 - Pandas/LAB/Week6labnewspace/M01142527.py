"""
RECORD CHECK  -  my version
===========================

Name  :  Stefan Valev
Lane  :  IT
Date  :  7/11/2026

Run it:   python/python3 CSVDataframe.py
"""

import pandas as pd
import os
import matplotlib.pyplot as plt


df = pd.DataFrame(pd.read_csv("/Users/stefan/Programming_stuff/Github_stuff/CST1510/Week 06 - Pandas/LAB/records_sample.csv"))

df["percent"] = (df["usedGB"] / df["totalGB"]) * 100
df["status"] = df["percent"].apply(lambda p: "OVER LIMIT" if p >= 100 else ("WARNING" if p >= 90 and p < 100 else "OK"))



# ================================================================== OUTPUT
# 3. Print the DataFrame.
#
#    Threshold : print it as-is, with the percent column.
#    Typical   : also filter to show only the rows that are not "OK", using a
#                boolean condition in [] - not a loop.
#    Excellent : also group by "status" and print a count per group, save
#                the full DataFrame to a new CSV with .to_csv(), and save
#                one bar chart of the counts per status.

# Threshold:
print (df)

# Typical:
print (df[df["status"] != "OK"])

# Excellent:
print(df.groupby("status").size())

df.to_csv("Datafram.csv", index=False)

counts = df["status"].value_counts()
counts.plot(kind="bar", rot=0)
plt.show()