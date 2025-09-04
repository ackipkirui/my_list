# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------
# Task 1: Load and Explore Dataset
# -------------------------------
try:
    # Load Iris dataset
    df = sns.load_dataset('iris')
    print("Dataset loaded successfully!")
except:
    print("Error loading dataset")

# Show first 5 rows
print(df.head())

# Check data info and missing values
print(df.info())
print(df.isnull().sum())

# Clean dataset (drop missing values if any)
df = df.dropna()

# -------------------------------
# Task 2: Basic Data Analysis
# -------------------------------

# Basic statistics of numerical columns
print(df.describe())

# Mean of numerical columns by species
print(df.groupby('species').mean())

# -------------------------------
# Task 3: Data Visualization
# -------------------------------

# 1. Line Chart: Petal Length trend
plt.plot(df.index, df['petal_length'], color='blue')
plt.title('Petal Length Trend')
plt.xlabel('Sample Index')
plt.ylabel('Petal Length')
plt.show()

# 2. Bar Chart: Average Petal Length per Species
sns.barplot(x='species', y='petal_length', data=df)
plt.title('Average Petal Length per Species')
plt.show()

# 3. Histogram: Sepal Length distribution
plt.hist(df['sepal_length'], bins=10, color='green')
plt.title('Sepal Length Distribution')
plt.xlabel('Sepal Length')
plt.ylabel('Frequency')
plt.show()

# 4. Scatter Plot: Sepal Length vs Petal Length
sns.scatterplot(x='sepal_length', y='petal_length', hue='species', data=df)
plt.title('Sepal vs Petal Length')
plt.show()
