import pandas as pd
from scipy import stats

# Load the dataset
df = pd.read_csv('sleep.csv')

# Specify the independent and dependent variables
X = df['Tot_hrs']
Y = df['SUM']

# Perform linear regression
slope, intercept, r_value, p_value, std_err = stats.linregress(X, Y)

# Interpret the results
print(f"Slope: {slope:.2f}")
print(f"Intercept: {intercept:.2f}")
print(f"Pearson's correlation coefficient: {r_value:.2f}")
print(f"P-value: {p_value:.2f}")

if p_value < 0.05:
    print("The linear relationship is statistically significant.")
else:
    print("The linear relationship is not statistically significant.")
