import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

# -------------------------------------------------------------------
# STEP 1: Load and Inspect the Dataset
# -------------------------------------------------------------------
df = pd.read_csv('/content/supply_chain_data.csv')

print("--- Data Summary ---")
print(df.info())
print("\n--- Missing Values Check ---")
print(df.isnull().sum())
