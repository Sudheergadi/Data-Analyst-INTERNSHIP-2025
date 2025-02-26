import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import zipfile
from datetime import datetime

# Extract CSV from ZIP
zip_path = '/content/googleplaystore.csv (1).zip'
with zipfile.ZipFile(zip_path, 'r') as z:
    file_name = z.namelist()[0]  # First file in the ZIP
    df = pd.read_csv(z.open(file_name))


df.dropna(subset=['Rating', 'Size', 'Installs', 'Last Updated', 'Reviews'], inplace=True)


df = df[df['Size'].str.contains('M|k|G', regex=True)]
df['Size'] = df['Size'].replace({'M': '*1e6', 'k': '*1e3', 'G': '*1e9'}, regex=True).map(pd.eval).astype(float)

df['Installs'] = df['Installs'].str.replace('[+,]', '', regex=True).astype(int)
df['Reviews'] = df['Reviews'].str.replace(',', '').astype(float)


df['Last Updated'] = pd.to_datetime(df['Last Updated'])


filtered_df = df[(df['Rating'] >= 4.0) &
                 (df['Size'] >= 10 * 1e6) &
                 (df['Last Updated'].dt.month == 1)]


category_group = filtered_df.groupby('Category').agg({'Rating': 'mean', 'Reviews': 'sum', 'Installs': 'sum'})


top_categories = category_group.nlargest(10, 'Installs')



import pytz
ist = pytz.timezone('Asia/Kolkata')
current_time = datetime.now(ist).time()

if current_time >= datetime.strptime('15:00:00', '%H:%M:%S').time() and current_time <= datetime.strptime('17:00:00', '%H:%M:%S').time():
    # plotting code here
    fig, ax = plt.subplots(figsize=(12, 8))
    bar_width = 0.35
    index = np.arange(len(top_categories))

    bars1 = ax.bar(index, top_categories['Rating'], bar_width, label='Average Rating')
    bars2 = ax.bar(index + bar_width, top_categories['Reviews'], bar_width, label='Total Reviews')

    ax.set_xlabel('App Category')
    ax.set_ylabel('Values')
    ax.set_title('Average Rating and Total Review Count by App Category')
    ax.set_xticks(index + bar_width / 2)
    ax.set_xticklabels(top_categories.index, rotation=45)
    ax.legend()
    plt.tight_layout()
    plt.show()
else:
    print("The graph is only available between 3 PM and 5 PM IST.")

