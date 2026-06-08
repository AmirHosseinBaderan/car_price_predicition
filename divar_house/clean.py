import pandas as pd 

df = pd.read_csv("./housing.csv")
print(f"Before : {df.shape}")


# normalize price column (remove spaces just in case)
df["Price"] = df["Price"].astype(str).str.strip()

# filter out "توافقی"
df = df[df["Price"] != "توافقی"]

print("After:", df.shape)


# save cleaned csv
df.to_csv("houses_cleaned.csv", index=False, encoding="utf-8-sig")

print("Saved: houses_cleaned.csv")