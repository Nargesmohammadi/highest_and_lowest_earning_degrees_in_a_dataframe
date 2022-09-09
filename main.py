import pandas as pd

df = pd.read_csv('003 salaries-by-college-major.csv')
print(df.head())

print(df.shape)

print(df.isna())

print(df.tail())

clean_df = df.dropna()
print(clean_df.tail())

print(clean_df['Starting Median Salary'])

highest = clean_df['Starting Median Salary'].max()
print(highest)

largest_value = clean_df['Starting Median Salary'].idxmax()
print(largest_value)

name_of_the_major = clean_df['Undergraduate Major'].loc[43]
print(name_of_the_major)

print(clean_df.loc[43])

# the highest mid-career salary:
highest_Mid_Career_Median_Salary = clean_df['Mid-Career Median Salary'].max()
print(highest_Mid_Career_Median_Salary)
print(f"the index for the max mid career salary: {clean_df['Mid-Career Median Salary'].idxmax()}")
print(clean_df['Undergraduate Major'][8])

# the lowest starting major and mid-career salary:
lowest_starting_and_mid_career = clean_df['Starting Median Salary'].min()
print(lowest_starting_and_mid_career)
print(clean_df['Undergraduate Major'].loc[clean_df['Starting Median Salary'].idxmax()])

# the lowest mid-career salary and how much can people expect to earn with this degree:
print(clean_df.loc[clean_df['Mid-Career Median Salary'].idxmax()])


# calculate the difference between the earnings of the 10th and 90th percentile:
print(clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary'])
print(clean_df['Mid-Career 90th Percentile Salary'].subtract(clean_df['Mid-Career 10th Percentile Salary']))


# adding the new column(spread) that is the result of the above calculation, with .insert():
spread_col = clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']
clean_df.insert(1, 'Spread', spread_col)
print(clean_df.head())


low_risk = clean_df.sort_values('Spread')
print(low_risk)

print(low_risk[['Undergraduate Major', 'Spread']].head())

# major with the highest_potential:
highest_potential = clean_df.sort_values('Mid-Career 90th Percentile Salary', ascending=False)
print(highest_potential[['Undergraduate Major', 'Mid-Career 90th Percentile Salary']].head())

# Majors with the Greatest Spread in Salaries
highest_spread = clean_df.sort_values('Spread', ascending=False)
print(highest_spread[['Undergraduate Major', 'Spread']].head())


# count how many majors we have in each category:
print(clean_df.groupby('Group').count())

# to find the average salary by group:
print(clean_df.groupby('Group').mean())

pd.options.display.float_format = '{:,.2f}'.format
