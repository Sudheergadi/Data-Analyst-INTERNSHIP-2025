import pandas as pd
import matplotlib.pyplot as plt
import datetime

# Load dataset
df = pd.read_csv("/content/apps.csv.zip")

# Data Cleaning & Filtering
df["Installs"] = df["Installs"].str.replace(",", "").str.replace("+", "").astype(float)
df["Price"] = df["Price"].replace("0", "0.0").str.replace("$", "").astype(float)
df["Revenue"] = df["Installs"] * df["Price"]
df["Size"] = pd.to_numeric(df["Size"], errors="coerce")
df["Android Ver"] = df["Android Ver"].str.extract(r"(\d+\.\d+)").astype(float)

filtered_df = df[(df["Installs"] >= 10000) & (df["Revenue"] >= 10000) &
                 (df["Android Ver"] > 4.0) & (df["Size"] > 15) &
                 (df["Content Rating"] == "Everyone") &
                 (df["App"].str.len() <= 30)]

top_categories = filtered_df["Category"].value_counts().nlargest(3).index
filtered_df = filtered_df[filtered_df["Category"].isin(top_categories)]

grouped_df = filtered_df.groupby(["Category", "Type"]).agg({"Installs": "mean", "Revenue": "mean"}).reset_index()

# Time Restriction Logic
current_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)
start_time = current_time.replace(hour=13, minute=0, second=0, microsecond=0)
end_time = current_time.replace(hour=14, minute=0, second=0, microsecond=0)

if start_time <= current_time <= end_time:
    fig, ax1 = plt.subplots(figsize=(10, 6))
    ax1.bar(grouped_df["Category"], grouped_df["Installs"], color="skyblue", label="Avg Installs")
    ax1.set_ylabel("Average Installs", color="blue")
    ax1.tick_params(axis="y", labelcolor="blue")
    
    ax2 = ax1.twinx()
    ax2.plot(grouped_df["Category"], grouped_df["Revenue"], color="red", marker="o", label="Avg Revenue")
    ax2.set_ylabel("Average Revenue ($)", color="red")
    ax2.tick_params(axis="y", labelcolor="red")
    
    plt.title("Average Installs & Revenue for Top 3 App Categories (Paid Apps)")
    ax1.set_xlabel("App Category")
    plt.show()
else:
    print("Graph is not available outside 1 PM - 2 PM IST.")
