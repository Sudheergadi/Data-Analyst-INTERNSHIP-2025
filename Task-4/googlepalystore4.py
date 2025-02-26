pip install pandas plotly numpy pytz

import pandas as pd
import plotly.express as px
import numpy as np
from datetime import datetime
import pytz


df = pd.read_csv("/content/googleplaystore.csv (1).zip")
df.dropna(subset=["Category", "Installs"], inplace=True)
df = df[df["Installs"].str.replace("[+,]", "", regex=True).str.isnumeric()]
df["Installs"] = df["Installs"].str.replace("[+,]", "", regex=True).astype(int)
df = df[~df["Category"].str.startswith(("A", "C", "G", "S"))]

category_group = df.groupby("Category")["Installs"].sum().reset_index()
top_categories = category_group.nlargest(5, "Installs")
top_categories["Highlight"] = np.where(top_categories["Installs"] > 1_000_000, "Highlighted", "Normal")
def is_time_allowed():
    india_tz = pytz.timezone("Asia/Kolkata")
    current_time = datetime.now(india_tz).hour
    return 18 <= current_time < 20  
if is_time_allowed():
    fig = px.bar(
        top_categories,
        x="Category",
        y="Installs",
        color="Highlight",
        title="Top 5 App Categories by Installs (Filtered)",
        labels={"Installs": "Total Installs", "Category": "App Category"},
        color_discrete_map={"Highlighted": "red", "Normal": "blue"},
    )
    fig.show()
else:
    print("Visualization is only available between 6 PM - 8 PM IST.")
