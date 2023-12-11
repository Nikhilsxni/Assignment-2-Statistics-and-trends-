"""
Created on Wed Dec  6 22:50:32 2023

@author: Nikhil Soni
Student ID: 22045846
"""
import pandas as pd
import matplotlib.pyplot as plt

# Import DataFrame
data = pd.read_csv(r"C:\assigment 1, ADS\AGR_LAND.csv")

agriculture_data = pd.DataFrame(data)

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