Task 4: Interactive Choropleth Map for Global App Installs

Overview

This project visualizes global app installs using an interactive bar chart. The visualization is filtered based on specific criteria and is displayed only between 6 PM and 8 PM IST.

Features

Data Cleaning: Filters non-numeric install values and removes unwanted categories.

Category Selection: Displays the top 5 app categories by total installs.

Conditional Highlighting: Highlights categories with installs exceeding 1 million.

Time-Based Restriction: The graph is only visible between 6 PM - 8 PM IST.

Interactive Visualization: Uses Plotly for dynamic and user-friendly visualization.

Dataset

The dataset used is googleplaystore.csv, containing information about app installs, categories, and other metadata.

Installation & Setup

Install required dependencies:

pip install pandas plotly numpy pytz

Ensure the dataset googleplaystore.csv is available in the working directory.

Run the script interactive_app_installs.py.

Usage

The script will process the dataset, clean the data, and generate an interactive visualization.

If executed outside the allowed time window (6 PM - 8 PM IST), the script will notify the user.

Repository Structure

📂 Task-4
   ├── interactive_app_installs.py  # Python script for visualization
   ├── googleplaystore.csv          # Dataset
   ├── README.md                    # Documentation
   ├── visualization.png             # Sample output image

Sample Output



Author

This project is part of the Data Analyst Internship 2025 tasks.

License

This project is open-source under the MIT License.

