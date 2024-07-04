import pandas as pd
import matplotlib.pyplot as pl 
from mpl_toolkits.mplot3d import Axes3D
# Step 1: Read the CSV file into a DataFrame
df = pd.read_csv(r'C:\Users\91832\OneDrive\Desktop\int project\Financial Analytics data.csv')

# Print current column names to identify unnamed columns
print("Current column names:", df.columns)



# Display the first few rows of the DataFrame
print("First few rows of the DataFrame:")
print(df.head())

# Display a summary of the DataFrame
print("\nDataFrame Info:")
print(df.info())

# Step 2: Perform changes (example manipulations below)
# Ensure the column exists before performing operations
if 'existing_column' in df.columns:
    # Adding a new column
    df['new_column'] = df['existing_column'] * 10

    # Filtering rows
    df_filtered = df[df['existing_column'] > 100]

    # Replacing values
   
    # Load the data
df = pd.read_csv('Financial Analytics data.csv', delimiter=',')
df.columns = df.columns.str.strip()  # Strip any extra spaces from column names

# Handle missing values
df['Sales Qtr - Crore'] = pd.to_numeric(df['Sales Qtr - Crore'], errors='coerce')  # Convert to numeric, making errors NaN
df.dropna(subset=['Sales Qtr - Crore'], inplace=True)  # Drop rows where Sales Qtr - Crore is NaN

# Set pandas options to display all rows and columns
pd.set_option('display.max_rows', None)  # None means show all rows
pd.set_option('display.max_columns', None)  # None means show all columns
pd.set_option('display.width', None)  # None means use maximum possible width to display

# Print the entire DataFrame
print(df)
# Print column names to verify them
print("Column names:", df.columns)

# Assuming the column name is exactly 'Mar Cap - Crore' after verifying
# Convert 'Mar Cap - Crore' to numeric, coercing errors to NaN
try:
    df['Mar Cap - Crore'] = pd.to_numeric(df['Mar Cap - Crore'], errors='coerce')
except KeyError:
    print("Column 'Mar Cap - Crore' does not exist. Check the column names printed above.")

# Handle missing values by dropping rows where 'Mar Cap - Crore' is NaN
df.dropna(subset=['Mar Cap - Crore'], inplace=True)

# Define bins for 'Low', 'Medium', 'High' categories
bins = [0, 10000, 50000, float('inf')]  # Adjust these values based on your data and requirements
labels = ['Low', 'Medium', 'High']

# Categorize 'Mar Cap - Crore' into 'Low', 'Medium', 'High'
df['Cap Size'] = pd.cut(df['Mar Cap - Crore'], bins=bins, labels=labels)

# Print results to verify
print(df[['Name', 'Mar Cap - Crore', 'Cap Size']]) 
# Optionally, check the distribution of categories
print(df['Cap Size'].value_counts())
# Print column names to verify them
print("Column names:", df.columns)

# Assuming the column name is exactly 'Mar Cap - Crore' after verifying
# Convert 'Mar Cap - Crore' to numeric, coercing errors to NaN
try:
    df['Mar Cap - Crore'] = pd.to_numeric(df['Mar Cap - Crore'], errors='coerce')
except KeyError:
    print("Column 'Mar Cap - Crore' does not exist. Check the column names printed above.")

# Convert 'Sales Qtr - Crore' to numeric, coercing errors to NaN
try:
    df['Sales Qtr - Crore'] = pd.to_numeric(df['Sales Qtr - Crore'], errors='coerce')
except KeyError:                            
    print("Column 'Sales Qtr - Crore' does not exist. Check the column names printed above.")

# Handle missing values by dropping rows where 'Mar Cap - Crore' or 'Sales Qtr - Crore' is NaN
df.dropna(subset=['Mar Cap - Crore', 'Sales Qtr - Crore'], inplace=True)

# Define bins for 'Low', 'Medium', 'High' categories  
bins = [0, 10000, 50000, float('inf')]  # Adjust these values based on your data and requirements
labels = ['Low', 'Medium', 'High']

# Categorize 'Mar Cap - Crore' into 'Low', 'Medium', 'High'
df['Cap Size'] = pd.cut(df['Mar Cap - Crore'], bins=bins, labels=labels)

# Sort the DataFrame by 'Mar Cap - Crore' in descending order
df_sorted = df.sort_values(by='Mar Cap - Crore', ascending=False)

# Print results to verify
print(df_sorted[['Name', 'Mar Cap - Crore', 'Sales Qtr - Crore', 'Cap Size']])


mean_sales = df_sorted['Sales Qtr - Crore'].mean()
print(f"Mean Sales Qtr: {mean_sales:.2f}")
 # Strip any extra spaces from column name
 # # Convert columns to numeric, coercing errors to NaN
df['Mar Cap - Crore'] = pd.to_numeric(df['Mar Cap - Crore'], errors='coerce')
df['Sales Qtr - Crore'] = pd.to_numeric(df['Sales Qtr - Crore'], errors='coerce')

# Drop rows with NaN values in 'Mar Cap - Crore' or 'Sales Qtr - Crore'
df.dropna(subset=['Mar Cap - Crore', 'Sales Qtr - Crore'], inplace=True)

# Define bins and labels for 'Mar Cap - Crore'
mar_cap_bins = [0, 10000, 50000, float('inf')]
mar_cap_labels = ['Low', 'Medium', 'High']

# Categorize 'Mar Cap - Crore'
df['Mar Cap Category'] = pd.cut(df['Mar Cap - Crore'], bins=mar_cap_bins, labels=mar_cap_labels)

# Sort the DataFrame by 'Mar Cap - Crore' in descending order
df_sorted = df.sort_values(by='Mar Cap - Crore', ascending=False)

# Define bins and labels for 'Sales Qtr - Crore' based on sorted 'Mar Cap - Crore'
sales_qtr_bins = [0, 100, 500, float('inf')]  # Adjust these values based on your data
sales_qtr_labels = ['Low', 'Medium', 'High']

# Categorize 'Sales Qtr - Crore'
df_sorted['Sales Qtr Category'] = pd.cut(df_sorted['Sales Qtr - Crore'], bins=sales_qtr_bins, labels=sales_qtr_labels)

# Print results to verify
print(df_sorted[['Name', 'Mar Cap - Crore', 'Mar Cap Category', 'Sales Qtr - Crore', 'Sales Qtr Category']])


# Print the DataFrame in the specified order
df.columns = df.columns.str.strip()  # Strip any extra spaces from column names

# Convert columns to numeric, coercing errors to NaN
df['Mar Cap - Crore'] = pd.to_numeric(df['Mar Cap - Crore'], errors='coerce')
df['Sales Qtr - Crore'] = pd.to_numeric(df['Sales Qtr - Crore'], errors='coerce')

# Drop rows with NaN values in 'Mar Cap - Crore' or 'Sales Qtr - Crore'
df.dropna(subset=['Mar Cap - Crore', 'Sales Qtr - Crore'], inplace=True)

# Define bins and labels for 'Mar Cap - Crore'
mar_cap_bins = [0, 10000, 50000, float('inf')]
mar_cap_labels = ['Low', 'Medium', 'High']

# Categorize 'Mar Cap - Crore'
df['Mar Cap Category'] = pd.cut(df['Mar Cap - Crore'], bins=mar_cap_bins, labels=mar_cap_labels)

# Sort the DataFrame by 'Mar Cap - Crore' in descending order
df_sorted = df.sort_values(by='Mar Cap - Crore', ascending=False)

# Calculate max, min, and median for 'Sales Qtr - Crore'
max_sales_qtr = df_sorted['Sales Qtr - Crore'].max()
min_sales_qtr = df_sorted['Sales Qtr - Crore'].min()
median_sales_qtr = df_sorted['Sales Qtr - Crore'].median()

# Define bins and labels for 'Sales Qtr - Crore' based on calculated values
sales_qtr_bins = [min_sales_qtr, median_sales_qtr, max_sales_qtr, float('inf')]
sales_qtr_labels = ['Low', 'Medium', 'High']

# Categorize 'Sales Qtr - Crore'
df_sorted['Sales Qtr Category'] = pd.cut(df_sorted['Sales Qtr - Crore'], bins=sales_qtr_bins, labels=sales_qtr_labels, include_lowest=True)

# Define the order for printing
order = [
    ('High', 'High'),
    ('Medium', 'High'),
    ('Low', 'High'),
    ('High', 'Medium'),
    ('Medium', 'Medium'),
    ('Low', 'Medium'),
    ('High', 'Low'),
    ('Medium', 'Low'),
    ('Low', 'Low')
]

# Print the DataFrame in the specified order
for mar_cap, sales_qtr in order:
    filtered_df = df_sorted[(df_sorted['Mar Cap Category'] == mar_cap) & (df_sorted['Sales Qtr Category'] == sales_qtr)]
    print(f"\n{mar_cap} Mar Cap with {sales_qtr} Sales Qtr:")
    print(filtered_df[['Name', 'Mar Cap - Crore', 'Mar Cap Category', 'Sales Qtr - Crore', 'Sales Qtr Category']])
print(df)

# Print 'Name' and 'Sales Qtr - Crore' columns together
print(df[['Name', 'Sales Qtr - Crore']])

# Print 'Name' and 'Sales Qtr - Crore' columns together
print(df[['Name', 'Mar Cap - Crore']])

# Assuming df is the DataFrame you have processed
# Calculate market cap ratio and add it as a new column
df['Market Cap to sale ratio'] = df['Mar Cap - Crore'] / df['Sales Qtr - Crore']
# Assuming df is the DataFrame you want to remove unnamed columns from
# Filter and drop columns containing 'Unnamed'
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

# Print the DataFrame after removing unnamed columns
print(df)

# Define low and high values for market cap ratio

print(df[['Name', 'Mar Cap - Crore', 'Sales Qtr - Crore', 'Market Cap to sale ratio']])
print(df)
# Check if the column exists before accessing it
if 'Market Cap to sale ratio' in df.columns:
    # Print summary statistics of the 'Mar Cap to Sale Ratio' column
    print(df['Market Cap to sale ratio'].describe())
else:
    print("Market cap to sale ratio' not found in the DataFrame.")
print(df)

import matplotlib.pyplot as plt

# Define quartile values
quartiles = [5.130256, 9.361662, 16.980167]
labels = ['25% = 5.130256', '50% = 9.361662', '75% = 16.980167']

# Create a bar graph with multiple bars
plt.bar(labels, quartiles, color=['blue', 'green', 'red'])

# Add labels and title
plt.xlabel('Quartiles')
plt.ylabel('Values')
plt.title('Summary Quartiles')

# Show the plot
plt.show()

import matplotlib.pyplot as plt

# Extract the required columns
x = df['Sales Qtr - Crore']
y = df['Mar Cap - Crore']

# Plot the line graph
plt.plot(x, y, marker='o', label='Market Cap to Sale Ratio')

# Add labels and title
plt.xlabel('Sales Qtr - Crore')
plt.ylabel('Mar Cap - Crore')
plt.title('Market Cap to Sale Ratio')

# Show the plot
plt.legend()
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Assuming 'Cap Size' is the categorical variable (modify if different)
df_plot = df.copy()

# Create a scatter plot with color based on 'Cap Size'
plt.scatter(df_plot['Sales Qtr - Crore'], df_plot['Mar Cap - Crore'], c=df_plot['Market Cap to sale ratio'], cmap='viridis')

# Add labels and title
plt.xlabel('Sales Qtr - Crore')
plt.ylabel('Mar Cap - Crore')
plt.title('Market Cap to sale ratio')



# Show the plot
plt.show()


# Assuming 'Mar Cap Category' is for sales (modify if different)
sales_by_category = df.groupby('Mar Cap Category')['Sales Qtr - Crore'].sum()

# Create a bar graph
plt.bar(sales_by_category.index, sales_by_category.values)

# Add labels and title
plt.xlabel('Market Cap Category')
plt.ylabel('Total Sales (Crore)')
plt.title('Total Sales by Market Cap Category')

# Show the plot
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.show()


# Assuming 'Mar Cap Category' is for company distribution (modify if different)
company_count_by_category = df['Mar Cap Category'].value_counts()

# Create a pie chart
plt.pie(company_count_by_category.values, labels=company_count_by_category.index, autopct="%1.1f%%")

# Add title
plt.title('Distribution of Companies by Market Cap Category')

# Show the plot
plt.show()
