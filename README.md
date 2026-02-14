# 🏠 Boston Housing Analysis: Beyond the Surface 🌊

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-blue?style=for-the-badge&logo=python&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)

> **"Does a river view actually add value?"** > This project moves beyond simple visualization to apply **rigorous statistical testing** and **data engineering** to the classic Boston Housing Dataset.

---

## 🎯 Project Overview
The goal was to identify the true drivers of property value (`MEDV`) in Boston. While many assume location is everything, this analysis uses Python to quantify the impact of room counts, socio-economic status, and river proximity.

### 🛠️ Key Technical Features
* [cite_start]**Data Engineering:** Handled `CRIM` outliers using the **IQR (Interquartile Range) Method**[cite: 5].
* [cite_start]**Feature Scaling:** Standardized numerical features using `StandardScaler` for model readiness[cite: 5].
* [cite_start]**Statistical Rigor:** Conducted an **Independent T-Test** to validate the impact of the Charles River (`CHAS`)[cite: 5].
* [cite_start]**Correlation Mapping:** Identified `RM` (Rooms) and `LSTAT` (Status) as the primary price drivers[cite: 5].

---

## 📊 Visual Gallery

### 1. The Value Drivers (Correlation Matrix)
By using a heatmap, we can clearly see the strong positive correlation between rooms and price, and the heavy inverse relationship with lower-status population density.

![Correlation Heatmap](Screenshot 2026-02-10 at 10.31.10 PM.jpg)

### 2. Room Count vs. Market Value
A regression analysis shows a clear linear trend: more rooms generally equal higher value, though we see interesting "caps" at the \$50k mark.

![Regression Plot](Screenshot 2026-02-10 at 10.31.19 PM.jpg)

### 3. The "River Effect" (Statistical Significance)
Our T-Test confirms that proximity to the Charles River is statistically significant ($p < 0.05$). The boxplot below highlights the higher median value for "River-bound" properties.

![River Impact Boxplot](Screenshot 2026-02-10 at 10.31.28 PM.jpg)

---

## 🧪 Statistical Results
| Test | Metric | Result |
| :--- | :--- | :--- |
| **T-Statistic** | `3.9964` | Significant |
| **P-Value** | `0.0001` | **Reject Null Hypothesis** |
| **Conclusion** | Proximity to River | **Strong Impact on Price** |

---

## 🚀 How to Run
1. Clone the repository:
   ```bashgit clone https://github.com/yourusername/boston-housing-analysis.git
