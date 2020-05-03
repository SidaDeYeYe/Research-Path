import os
import pandas as pd

all_files = os.listdir()
target_files = {}
for name in all_files:
    if name.endswith("Att.txt"):
        realname = name[:-7]
        target_files[realname] = name

#print(target_files)

result = {}
for (key, val) in target_files.items():
    df = pd.read_csv(val, delimiter='\t')
    man = len(df[df["gender"] == 1])
    woman = len(df[df["gender"] == 2])
    if man > woman:
        result[key] = "man"
    elif woman > man:
        result[key] = "woman"
    else:
        result[key] = "neutrality"

df = pd.read_csv("49report.csv")
df = df[df.columns.tolist()[:-2]]

new_column = []

for name in df["Network Name"]:
    print(name)
    name = name[:-3]
    if name in result.keys():
        target = result[name]
        new_column.append(target)
    else:
        print("Not found: " + name)
        new_column.append("")

df["Domination"] = new_column
df.to_csv("fbook.csv", index=False)