"""
Created on Mon Dec 11 01:29:12 2023

@author: Nikhil Soni
Student ID: 22045846
"""
import pandas as pd
import matplotlib.pyplot as plt

# Importing  data
urban_pop_df = pd.read_csv(r"C:\assignment 2 ads\urban_pop\urban_pop.csv")

# Display summary statistics of the DataFrame using describe() function
print("Summary Statistics of the DataFrame:")
print(urban_pop_df.describe())

# Plotting
plt.figure(figsize=(10, 6))

for country in urban_pop_df.columns[1:]:
    plt.plot(urban_pop_df['Year'], urban_pop_df[country], label=country)

# Set labels, title and legend
plt.title('Urban population over years')
plt.xlabel('Year')
plt.ylabel('% of Urban Population')
plt.legend()

# show the plot
plt.show()
