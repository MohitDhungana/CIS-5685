import pandas as pd

# a = [10, 30, 20]
# myseries = pd.Series(a)
# print(myseries)
# myseries = pd.Series(a, index=["x", "y", "z"])
# print(myseries)
# sales = {"Mon": 1020, "Tue": 989, "Wed": 998}
# myseries = pd.Series(sales)
# print(myseries)
# print(myseries["Tue"])
# # Create a Series using only data from "Mon" and "Wed"
# myseries = pd.Series(sales, index=["Mon", "Wed"])
# print(myseries)

# data = {"sales": [1020, 989, 998], "items": [50, 40, 45]}

# df = pd.DataFrame(data)
# print("df\n", df)
# print("df.loc[0]\n", df.loc[0])
# print("df.loc[[0, 1]]\n", df.loc[[0, 1]])
# # dataframe with named index
# df = pd.DataFrame(data, index=["Mon", "Tue", "Wed"])
# print("df\n", df)
# print("df.loc['Tue']\n", df.loc["Tue"])
# print("df['sales']\n", df["sales"])


df = pd.read_csv("Store11.csv")

print(df.head())
print(df.info())
print(df.describe())
