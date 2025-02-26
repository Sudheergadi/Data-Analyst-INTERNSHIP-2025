Google Play Store Apps Data Analysis

Overview

This project analyzes the Google Play Store dataset to compare the average rating and total review count for the top 10 app categories by the number of installs. The analysis is filtered to include only apps that:

Have an average rating of 4.0 or above

Have a size of at least 10 MB

Were last updated in January

Are displayed only between 3 PM - 5 PM IST on the dashboard

Features

Data Cleaning & Preprocessing: Handles missing values, converts data formats, and filters relevant apps.

Visualization: Uses a grouped bar chart to show ratings and review counts.

Time Restriction: Ensures the graph is visible only between 3 PM - 5 PM IST.

Dataset

The dataset used for this analysis is the Google Play Store Apps Dataset, which contains:

App Category

Rating

Size (in MB)

Installs

Last Updated Date

Total Reviews

Dataset Source

Google Play Store Dataset on Kaggle

Installation & Usage

1. Clone the Repository

    git clone https://github.com/Sudheergadi/Data-Analyst-INTERNSHIP-2025.git
    cd Data-Analyst-INTERNSHIP-2025

2. Install Dependencies

Ensure you have Python installed, then install the required libraries:

    pip install pandas matplotlib numpy pytz

3. Run the Script

    python analysis.py

Code Explanation

Data Extraction: Reads the dataset from a ZIP file.

Filtering Data: Removes unnecessary data and converts columns.

Aggregating Data: Groups by app category and calculates the average rating and total reviews.

Visualization: Generates a grouped bar chart.

Time Restriction: Displays the graph only between 3 PM - 5 PM IST.

Example Graph Output



License

This project is open-source under the MIT License. Feel free to contribute!

Contributors

Sudheer Gadi - GitHub Profile

