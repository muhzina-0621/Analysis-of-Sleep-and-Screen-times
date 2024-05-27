import pandas as pd
from scipy.stats import chi2_contingency

# Load the dataset
df = pd.read_csv('sleep.csv')
print(df)
# Create a contingency table
contingency_table = pd.crosstab(df['SUM'], df['Tot_hrs'])

# Perform chi-square test
chi2, p, dof, expected = chi2_contingency(contingency_table)
print()
# Interpret the results
if p < 0.05:
    print("There is a significant association between Screen time and Sleep Time.")
else:
    print("There is no significant association between Screen Time and Sleep.")
