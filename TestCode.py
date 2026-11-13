# Import necessities
import pandas as pd
import matplotlib.pyplot as plt

# Create DataFrame
memberData = pd.DataFrame ({
    "memberIndex": [1, 2, 3, 4, 5, 6],
    "memberName": ["John", "Smith", "Jennifer", "Conc R. ete", "River", "Ggs brev"],
    "workoutType": ["Cardio", "Yoga", "Yoga", "Strength", "Yoga", "Cardio"],
    "caloriesBurned": [500, 120, 450, 1250, 560, 592],
    "heartRate": [160, 80, 125, 152, 74, 148],
    "durationMins": [60, 28, 100, 120, 80, 77],
})

# Create and print new column "burnRateperMinute"
memberData["burnRateperMinute"] = memberData["caloriesBurned"] / memberData["durationMins"]
print (memberData["memberName"], memberData["burnRateperMinute"])

# Use .iloc to print first row and .loc to print specific cell
print (memberData.iloc[2])
print (memberData.loc[3, "caloriesBurned"])

# Filter and print rows where durationMins >= 45
filteredDuration = memberData[memberData.apply(lambda row: row["durationMins"] >= 45, axis=1)]
print (filteredDuration)

# Use combined condition to find members who did Cardio with a heart rate of more than 150


