from scipy import stats
import pandas as pd

# Load the dataset
df = pd.read_csv('sleep.csv')

# Split the data into two groups
group_a = df[df['SUM'] == 'A']['SUM']
group_b = df[df['Tot_hrs'] == 'B']['Tot_hrs']


# Perform independent sample t-test
t_statistic, p_value = stats.ttest_ind(group_a, group_b)
# Interpret the results

if p_value < 0.05:
    print("There is a significant difference between Sleep time  and Screen time.")
else:
    print("There is no significant difference between Screen time and Sleep.")
