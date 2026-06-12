import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Loading the data
data = sns.load_dataset("iris")

# Inspection of data 
print(f"Shape of data: {data.shape}")
print(f"Column names: {list(data.columns)}")

print("\n--- First 15 Rows --- ")
print(data.head(15))

print("\n--- Dataset Info --- ")
print(data.info())

print("\n--- Summary Statistics --- ")
print(data.describe())

# Data visualization
# Scatterplot
plt.figure(figsize=(8, 5))
sns.scatterplot(x="sepal_length", y="petal_length", data=data, hue="species")
plt.title("Sepal Length VS Petal Length across Iris Species")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.tight_layout()
plt.show()

# Histogram
plt.figure(figsize=(8, 5))
sns.histplot(x="sepal_length", data=data, hue="species", bins=10)
plt.title("Distribution of Sepal Length by Species")
plt.xlabel("Sepal Length (cm)")
plt.tight_layout()
plt.show()

# Boxplot
plt.figure(figsize=(8, 5))
sns.boxplot(x="species", y="sepal_length", data=data, hue="species", palette="pastel")
plt.title("Sepal Length Distribution & Outliers by Species")
plt.xlabel("Species")
plt.ylabel("Sepal Length (cm)")
plt.tight_layout()
plt.show()

