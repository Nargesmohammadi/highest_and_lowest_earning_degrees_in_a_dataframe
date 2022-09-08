import pandas as pd

df = pd.read_csv('003 salaries-by-college-major.csv')
# print 5 first rows.
print(df.head())


# print the all rows.
print(df.shape)


# to see the number of rows and columns.
print(df.isna())

# to print the 5 last rows.
print(df.tail())


# to delete the last row of cv.
clean_df = df.dropna()
print(clean_df.tail())

# to  see all the values printed out below the cell for just this column
print(clean_df['Starting Median Salary'])


# to find the highest starting salary
highest = clean_df['Starting Median Salary'].max()
print(highest)

# index for the row with the largest value
largest_value = clean_df['Starting Median Salary'].idxmax()
print(largest_value)

# To see the name of the major that corresponds to that particular row, we can use the .loc (location) property.
name_of_the_major = clean_df['Undergraduate Major'].loc[43]
print(name_of_the_major)

# If you don't specify a particular column you can use the .loc property to retrieve an entire row.
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
