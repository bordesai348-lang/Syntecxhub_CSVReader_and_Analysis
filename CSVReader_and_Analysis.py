import pandas as pd

print("\n--- Project 2: Pandas CSV Reader & Basic Analysis ---")


data = { "Name": ["A", "B", "C", "D"], "Age": [20, 21, 22, 21], "Marks": [85, 90, 78, 88] }

df = pd.DataFrame(data) df.to_csv("students.csv", index=False)



df = pd.read_csv("students.csv") print("Head:\n", df.head()) print("Tail:\n", df.tail()) print("Data Types:\n", df.dtypes)


print("Summary Stats:\n", df.describe()) print("Mean Marks:", df["Marks"].mean()) print("Max Age:", df["Age"].max())


filtered_df = df[df["Marks"] > 80][["Name", "Marks"]] print("Filtered Data:\n", filtered_df)


filtered_df.to_csv("filtered_students.csv", index=False)

