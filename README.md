# Task 1: Exploratory Data Analysis (EDA) on the Iris Dataset

This repository contains my solution for Task 1 of my AI/ML Engineering Internship at Developers Hub Cooperation. The objective of this project is to load, inspect, and visualize a classic dataset to understand data trends, feature distributions, and uncover patterns.

## Features Covered
- **Data Inspection:** Utilizing `pandas` to analyze shape, feature types, and descriptive statistics (`.head()`, `.info()`, `.describe()`).
- **Data Visualization:** Built using `seaborn` and `matplotlib`:
  - **Scatter Plot:** Analyzing the relationship between sepal length and petal length.
  - **Histogram:** Visualizing the frequency distribution of sepal lengths across different species.
  - **Box Plot:** Statistical distributions and outlier detection for feature sets.

## Technologies Used
- Python 3
- Pandas
- Matplotlib
- Seaborn

## How to Run
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the script: `python main.py`

## Key Insights & Final Conclusions
After performing an Exploratory Data Analysis on the Iris dataset, the following key findings were observed:

* **Distinct Feature Clusters:** The scatter plots demonstrate that *Iris setosa* is easily distinguishable from other species based on petal dimensions, which will make it a high-performing class for any classification model.
* **Data Quality:** The box plots confirm that the dataset is well-structured and free of significant outliers, ensuring that a model trained on this data will be stable and reliable.
* **Predictive Potential:** The clear separation of the species clusters across various feature visualizations indicates that the dataset is highly suitable for building accurate classification algorithms in subsequent tasks.
