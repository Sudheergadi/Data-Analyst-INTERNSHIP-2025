# Data Analyst Internship - Task 01 📊

## 🔥 Task Overview
This project focuses on analyzing **5-star reviews** of **Health & Fitness apps** from the Google Play Store dataset. The goal is to extract **the most frequent keywords**, remove common stopwords, and create a **Word Cloud visualization**.

## 📂 Dataset
- **Source**: Google Play Store
- **Filtered Data**: Contains only **Health & Fitness** category apps.
- **File**: `health_fitness_apps.csv`

## ⚡ Steps in the Analysis:
1. **Data Cleaning**
   - Removed unnecessary columns
   - Filtered apps only in the **Health & Fitness** category
   - Removed stopwords and app names from reviews

2. **Data Analysis**
   - Extracted **5-star reviews**
   - Tokenized words and counted **frequencies**
   - Removed unnecessary words (stopwords, app names)

3. **Visualization**
   - Generated a **Word Cloud** to show frequently mentioned words in reviews.

## 🛠️ Requirements
To run the analysis, install these Python libraries:

```bash
pip install pandas wordcloud nltk matplotlib
