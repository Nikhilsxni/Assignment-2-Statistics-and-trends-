"""
Created on Wed Dec  6 22:50:32 2023

@author: Nikhil Soni
Student ID: 22045846
"""
import pandas as pd
import matplotlib.pyplot as plt

def describe(data_frame):
    """Print summary statistics of the DataFrame."""
    print(data_frame.describe())

# Import DataFrame
data = pd.read_csv(r"C:\assignment 2 ads\Agr_land\AGR_LAND.csv")
agriculture_data = pd.DataFrame(data)

# Call describe function
describe(agriculture_data)

# Plotting using Pandas
agriculture_data.set_index('Country Name', inplace=True)
agriculture_data.drop('Year', axis=1, inplace=True)  # Remove 'Year' column for plotting

# Transpose the DataFrame for a better plot
agriculture_data_transposed = agriculture_data.transpose()

# Plotting
ax = agriculture_data_transposed.plot(kind='bar', figsize=(10, 6), colormap='viridis')

# Set labels and title
plt.xlabel('Year')
plt.ylabel('Percentage')
plt.title('Agriculture land % by year(2015-2021)')

# Show the plot
plt.show()
