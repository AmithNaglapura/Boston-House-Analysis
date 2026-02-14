import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.preprocessing import StandardScaler

# --- SECTION 1: DATA LOADING & SUMMARY ---
# The dataset contains 506 entries and 14 features[cite: 5, 27].
df = pd.read_csv('boston.csv') 

print(f"Dataset Shape: {df.shape}")
print("\nMissing values per column:\n", df.isnull().sum())

# --- SECTION 2: EXPLORATORY DATA ANALYSIS (EDA) ---
sns.set_theme(style="whitegrid")

# 2.1 Distribution of Home Values
# This shows the spread of prices and the 'capped' values at 50[cite: 5].
plt.figure(figsize=(8, 5))
sns.histplot(df['MEDV'], kde=True, color='blue')
plt.title('Distribution of Median Home Values (MEDV)')
plt.show()

# 2.2 Feature Correlation Matrix
# This explains which variables like Rooms (RM) or Status (LSTAT) drive the price[cite: 5].

plt.figure(figsize=(12, 8))
correlation_matrix = df.corr().round(2)
sns.heatmap(data=correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('How Housing Factors Relate to Each Other')
plt.show()

# 2.3 Scatter Plot: Rooms vs Price
# Directly visualizes the strongest predictor of value[cite: 5].
plt.figure(figsize=(8, 6))
sns.regplot(x='RM', y='MEDV', data=df, scatter_kws={'alpha':0.5}, line_kws={'color':'red'})
plt.title('Relationship Between Number of Rooms and House Value')
plt.show()

# --- SECTION 3: DATA CLEANING & ENGINEERING ---
# Handling Outliers in Crime Rate (CRIM) using the Interquartile Range (IQR)[cite: 5].
Q1 = df['CRIM'].quantile(0.25)
Q3 = df['CRIM'].quantile(0.75)
IQR = Q3 - Q1
outliers = df[(df['CRIM'] < (Q1 - 1.5 * IQR)) | (df['CRIM'] > (Q3 + 1.5 * IQR))]
print(f"Number of outliers detected in CRIM: {len(outliers)}")

# Scaling features to ensure they are on the same mathematical scale.
scaler = StandardScaler()
features_to_scale = df.drop(columns=['MEDV', 'CHAS']).columns
df[features_to_scale] = scaler.fit_transform(df[features_to_scale])

# --- SECTION 4: HYPOTHESIS & SIGNIFICANCE TESTING ---
# Hypothesis: Does proximity to the Charles River (CHAS) increase home value (MEDV)? [cite: 5]
river_bound = df[df['CHAS'] == 1]['MEDV']
not_river_bound = df[df['CHAS'] == 0]['MEDV']

t_stat, p_val = stats.ttest_ind(river_bound, not_river_bound)

print(f"\n--- Significance Test Results ---")
print(f"T-statistic: {t_stat:.4f}")
print(f"P-value: {p_val:.4f}")

if p_val < 0.05:
    print("Result: Significant. River proximity affects price.")
else:
    print("Result: Not significant.")

# Visualizing the Significance Test
plt.figure(figsize=(6, 4))
sns.boxplot(x='CHAS', y='MEDV', data=df)
plt.title('Impact of Charles River Proximity on Home Value')
plt.xticks([0, 1], ['No River', 'River'])
plt.show()