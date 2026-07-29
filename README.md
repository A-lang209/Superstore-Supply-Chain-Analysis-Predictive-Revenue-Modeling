# Supply-Chain-Data-Analysis

# 📦 Superstore End-to-End Supply Chain & Predictive Revenue Analysis

## 📌 Project Overview
This project performs an end-to-end Exploratory Data Analysis (EDA) and Predictive Modeling on a Superstore supply chain dataset. The objective is to evaluate key operational metrics across product catalog performance, shipping carrier efficiency, supplier quality control, and evaluate linear regression modeling for revenue prediction.

---

## 🔑 Key Features & Findings
- **Data Analysis & Viz:** Evaluated revenue streams across product lines (`Skincare`, `Haircare`, `Cosmetics`) and analyzed shipping lead times and defect rates.
- **Logistics Efficiency:** Analyzed shipping costs and transit times across transport modes (Air, Road, Rail, Sea) and carriers.
- **Quality Control Tracking:** Evaluated supplier inspection failure/pass rates and defect frequencies.
- **Predictive Modeling:** Built an **Ordinary Least Squares (OLS) Linear Regression** model using Scikit-Learn to predict revenue generated from 14 operational features.

---

## 📊 Predictive Model Evaluation
- **Algorithm:** Linear Regression
- **Train/Test Split:** 80% / 20%
- **Evaluation Metrics:**
  - **Testing $R^2$ Score:** `-0.4939`
  - **Testing RMSE:** `$3,464.83`

### Operational Key Takeaway
The linear model revealed low direct correlation between feature variables (e.g., `Price` and `Units Sold`) and `Revenue Generated` due to synthetic generation within the dataset. Future iterations will explore non-linear ensemble models (Random Forest, XGBoost) and custom feature engineering ($\text{Price} \times \text{Quantity}$).

---

## 🛠️ Tech Stack & Libraries
- **Language:** Python 3.10+
- **Data Manipulation:** `pandas`, `numpy`
- **Data Visualization:** `matplotlib`, `seaborn`
- **Machine Learning:** `scikit-learn`
   ```bash
   git clone [https://github.com/YOUR_USERNAME/Supply-Chain-Data-Analysis.git](https://github.com/YOUR_USERNAME/Supply-Chain-Data-Analysis.git)
   cd Supply-Chain-Data-Analysis
