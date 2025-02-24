Data Analyst Internship Project

Overview

This project analyzes app installs and revenue data to generate a dual-axis graph comparing average installs and revenue for free vs. paid apps in the top 3 app categories. The graph is displayed only between 1 PM and 2 PM IST.

Dataset

The dataset (apps.csv) contains details about various apps, including category, installs, price, revenue, and more. Filters applied include:

Minimum 10,000 installs

Minimum $10,000 revenue

Android version > 4.0

Size > 15MB

Content rating: Everyone

App name length ≤ 30 characters

Features

Cleans and filters data based on criteria

Identifies top 3 categories by number of apps

Plots a dual-axis graph (bar chart for installs, line chart for revenue)

Restricts visibility to 1 PM - 2 PM IST

Usage

Run the script using:

python script.py

Ensure apps.csv is present in the same directory.

Dependencies

pandas

matplotlib

Install dependencies using:

pip install pandas matplotlib

