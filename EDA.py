import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Load built-in dataset
df = sns.load_dataset('tips')

# 2. Basic Inspection
print("--- Data Info ---")
print(df.info())
print("\n--- Statistical Summary ---")
print(df.describe())

# 3. Correlation Analysis (Numeric only)
plt.figure(figsize=(8, 4))
sns.heatmap(df.select_dtypes(include=['number']).corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

# 4. Visualizing Trends: Total Bill vs Tip by Gender
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='total_bill', y='tip', hue='day', style='time')
plt.title('Relationship: Bill vs Tip (by Day & Time)')
plt.show()

# 5. Identifying Distribution: Tips by Day
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x='day', y='total_bill', palette='Set2')
plt.title('Revenue Distribution by Day')
plt.show()