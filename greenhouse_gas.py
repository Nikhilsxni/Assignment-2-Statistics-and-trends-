"""
Created on Tue Dec 12 00:11:11 2023

@author: NIKHIL SONI
Student id: 22045846
"""

import pandas as pd
import matplotlib.pyplot as plt


# Create a DataFrame
greenhouse_gas_df = pd.read_csv(r"C:/assignment 2 ads/greenhouse_gas/greenhouse_gas_emi.csv")

# Display summary statistics
print(greenhouse_gas_df.describe())

# Plotting pie charts
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Plotting pie chart for 2000
greenhouse_gas_df.plot.pie(y='2000', labels=greenhouse_gas_df['Country Name'],
            autopct='%1.1f%%', startangle=90, ax=axes[0], legend=False)
axes[0].set_title('Greenhouse Gas Emissions in 2000')
axes[0].legend(greenhouse_gas_df['Country Name'], loc='upper left', bbox_to_anchor=(1, 1))

# Plotting pie chart for 2010
greenhouse_gas_df.plot.pie(y='2010', labels=greenhouse_gas_df['Country Name'],
            autopct='%1.1f%%', startangle=90, ax=axes[1], legend=False)
axes[1].set_title('Greenhouse Gas Emissions in 2010')
axes[1].legend(greenhouse_gas_df['Country Name'], loc='upper left', bbox_to_anchor=(1, 1))

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()
